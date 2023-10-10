#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import reduce


def is_even(n):
    return n % 2 == 0


def repeat(n, times):
    return [n] * times


def concat(list_a, list_b):
    return [*list_a, *list_b]


def computed():
    numbers = range(1, 8)
    evens = filter(is_even, numbers)
    repeats = map(lambda n: repeat(n, n), evens)
    values = reduce(concat, repeats, [])
    return values


print(computed())
# > python compute.py
# [2, 2, 4, 4, 4, 4, 6, 6, 6, 6, 6, 6]
