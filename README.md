# Kedro-Pandas-Profiling

This is a Kedro plugin that uses [Pandas-Profiling](https://github.com/pandas-profiling/pandas-profiling) to profile datasets.

## Installation

It can be installed via PyPI.

``` sh
pip install kedro-pandas-profiling

```

## How is Kedro-Pandas Profiling Used?
You simply proceed with a Kedro project as normal.

Once the data catalog is set up, you can run:

``` sh
kedro profile #this returns the list of things in the catalog

kedro profile -n #with the name of the dataset
```

Kedro profile with no arguments returns the results of your catalog,
and from that you can append a name of a dataset to profile. This 
current iteration only supports .csv and .xlsx files.

### Sample Output:

Sample output based on the company dataset from the Kedro tutorial.

![Sample Output](https://github.com/BrickFrog/kedro-pandas-profiling/blob/master/samples/sample.PNG)

## What licence do you use?

Kedro-Pandas-Profiling is licensed under the [Apache 2.0](LICENSE) License.

