from click import ClickException
from click.testing import CliRunner
from kedro.config import ConfigLoader
from pathlib import Path
import pandas as pd
from pandas.util.testing import assert_frame_equal
from pyfakefs.fake_pathlib import FakePathlibModule
from unittest import mock
import pytest

from kedro_pandas_profiling.plugin import (
    kedro_conf_path,
    get_catalog_details,
    pd_reader,
    profile,
)

CONF_DICT = {
            "companies": {
                "type": "CSVLocalDataSet",
                "filepath": "data/01_raw/companies.csv",
            },
            "shuttles": {
                "type": "kedro_tutorial.io.xls_local.ExcelLocalDataSet",
                "filepath": "data/01_raw/shuttles.xlsx",
            },
        }


class MockConfig:
    """Custom clss to be the mock return value of ConifgLoader.get()"""

    @staticmethod
    def get_config_dict():
        """A faux config listing for pytest"""
        return CONF_DICT


@pytest.fixture
def mock_config(monkeypatch):
    """ConfigLoader.get() mocked to return faux data dictionary"""

    def mock_get(*args, **kwargs):
        return MockConfig.get_config_dict()

    monkeypatch.setattr(ConfigLoader, "get", mock_get)


def kedro_conf(mock_config):

    config = ConfigLoader(["conf/base", "conf/local"])
    config_dict = config.get("catalog*", "catalog*/**")

    return config_dict

#TODO: There might be a better way to handle this, fake data folder?
def test_get_config_details(mock_config):

    config = kedro_conf(mock_config)

    x = get_catalog_details(config)
    y = pd.DataFrame(CONF_DICT).T

    assert x.equals(y)

def test_pd_reader(mock_config):

    config = kedro_conf(mock_config)

    assert 0

