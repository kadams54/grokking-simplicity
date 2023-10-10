#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydash import py_


def is_even(n):
    return n % 2 == 0


def repeat(n, times):
    return [n] * times


def concat(list_a, list_b):
    return [*list_a, *list_b]


def computed():
    return (
        py_(py_.range(1, 8))
        .filter(is_even)
        .map(lambda n: repeat(n, n))
        .reduce(concat, [])
        .value()
    )


print(computed())
# > python compute-with-python.py
# [2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6]
