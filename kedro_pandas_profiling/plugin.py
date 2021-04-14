import click
from kedro.framework.cli import get_project_context
from kedro.config import ConfigLoader
import os
import pandas as pd
from pathlib import Path
import pandas_profiling


def kedro_conf_path() -> dict:
    config = ConfigLoader(["conf/base", "conf/local"])
    conf_catalog = config.get("catalog*", "catalog*/**")

    return conf_catalog


def get_catalog_details(conf_catalog) -> pd.DataFrame:
    """ Returns a DataFrame of the Kedro Catalog(s) """
    catalog_df = pd.DataFrame(conf_catalog).T

    return catalog_df


def pd_reader(filepath: Path) -> pd.DataFrame:
    """ Helper Function for Reading Pandas DataFrames """
    # TODO: Inelegant, Refactor

    extension = filepath.suffix

    if extension == ".csv":
        df = pd.read_csv(filepath)
    elif extension == ".xlsx":
        df = pd.read_excel(filepath)
    else:
        raise NotImplementedError(
            f"This file type '{extension}' has not been implemented yet."
        )

    return df


@click.group(name="Profiling")
def commands():
    """ Kedro plugin for profiling datasets """
    pass


@commands.command(name="profile")
@click.option(
    "--name",
    "-n",
    type=str,
    default=None,
    help="Dataset name for kedro to profile. "
    "Default lists the contents of the catalog",
)
def profile(name):
    """ Kedro plugin for utilizing Pandas Profiling """
    conf_dict = kedro_conf_path()
    catalog_df = get_catalog_details(conf_dict)
    project_path = get_project_context().project_path

    if name == None:
        print(catalog_df)
    else:
        data_path = catalog_df.at[name, "filepath"]
        data = pd_reader(project_path / data_path)

        print(f"Profiling {name} DataSet...")

        profile = data.profile_report(
            title=f"DataSet {name} - Profile Report", pool_size=0
        )

        output_path = Path.joinpath(project_path, f"data/08_reporting/{name}.html")
        profile.to_file(output_file=output_path)

        print(f"{name.title()} profile printed to {output_path}")

        return None

