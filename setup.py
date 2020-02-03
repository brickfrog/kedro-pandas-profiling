import re
from codecs import open
from os import path

from setuptools import setup

name = "kedro-pandas-profiling"
here = path.abspath(path.dirname(__file__))

# get package version
package_name = name.replace("-", "_")
with open(path.join(here, package_name, "__init__.py"), encoding="utf-8") as f:
    version = re.search(r'__version__ = ["\']([^"\']+)', f.read()).group(1)

# get the dependencies and installs
with open("requirements.txt", "r", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

# get test dependencies and installs
with open("test_requirements.txt", "r", encoding="utf-8") as f:
    test_requires = [x.strip() for x in f if x.strip() and not x.startswith("-r")]
   

setup(
    name=name,
    version=version,
    description="Kedro-Pandas-Profiling is a small Kedro plugin for profiling dataframes",
    long_description="Kedro-Pandas-Profiling is a small Kedro plugin that provides a wrapper to Pandas Profiling, allowing data in the catalog to be quickly profiled",
    url="https://github.com/brickfrog/kedro-pandas-profiling",
    license="Apache License 2.0",
    python_requires=">=3.6, <3.8",
    install_requires=requires,
    tests_require=test_requires,
    author="Justin Malloy",
    packages=["kedro_pandas_profiling"],
    entry_points={
        "kedro.project_commands": ["profiling = kedro_pandas_profiling.plugin:commands"]
    },
)
