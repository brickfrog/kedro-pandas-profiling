import click
from kedro.cli import get_project_context
from kedro.config import ConfigLoader
import os
import pandas as pd
from pathlib import Path
import pandas_profiling
from typing import Union

CONF_PATHS = ["conf/base", "conf/local"]


def _get_catalog_details(path: Union[str, list]) -> pd.DataFrame:
    """ Returns a DataFrame of the Kedro Catalog(s) """
    conf_loader = ConfigLoader(path)
    conf_catalog = conf_loader.get("catalog*", "catalog*/**")
    catalog_df = pd.DataFrame(conf_catalog).T

    return catalog_df


def _pd_reader(filepath: Path) -> pd.DataFrame:
    """ Helper Function for Reading Pandas DataFrames """
    # TODO: I believe there's a way to handle this with Kedro proper, Refactor

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
    catalog_df = _get_catalog_details(CONF_PATHS)
    project_path = get_project_context("project_path")

    if name == None:
        print(catalog_df)
    else:
        data_path = catalog_df.at[name, "filepath"]
        data = _pd_reader(project_path / data_path)

        print(f"Profiling {name} DataSet...")

        profile = data.profile_report(
            title=f"DataSet {name} - Profile Report", pool_size=0
        )

        output_path = Path.joinpath(project_path, f"data/08_reporting/{name}.html")
        profile.to_file(output_file=output_path)

        print(f"{name.title()} profile printed to {output_path}")

        return None

