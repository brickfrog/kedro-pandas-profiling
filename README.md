# Kedro-Pandas-Profiling

This is a simple plugin that uses [Pandas-Profiling](https://github.com/pandas-profiling/pandas-profiling) to profile datasets in the Kedro catalog.

## Installation

Currently not on Pypy, you can install directly from github.

**TODO**: Installation Notes.

## How is Kedro-Pandas Profiling Used?

You simply proceed with a Kedro project as normal, and once the data catalog is set up, you
can run:

```
kedro profile

kedro profile -n -name of dataset-
```

Kedro profile with no arguments returns the results of your catalog, and from that
you can append a name of a dataset to profile. This current interation only supports
.csv and .xlsx files.

### Sample Output:

This is a sample output based on the company dataset from the Kedro pipeline tutorial.

![Sample Output](/samples/sample.png)

## What licence do you use?

Kedro-Pandas-Profiling is licensed under the [Apache 2.0](LICENSE) License.