# Compute: Chaining Functions for Fun and Profit

Your challenge: write a program that implements these steps:

1. Generate a list of 1-8, not including 8: `[1, 2, 3, 4, 5, 6, 7]`
1. Filter that list to even values: `[2, 4, 6]`
1. Return each value N repeated N times: `[2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6]`

Running your `compute` program should output this:

```
[2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6]
```

## Python

There's a `pyproject.toml` file, so feel free to use that to spin up your
virtualenv however you prefer. Poetry users could simply run `poetry run
whatever-script.py`. Here are the current Python scripts:

- `compute.py`: Basic Python, no extra libs.
- `compute-with-pydash.py`: Uses [pydash](https://pydash.readthedocs.io/) to do
the chaining.

