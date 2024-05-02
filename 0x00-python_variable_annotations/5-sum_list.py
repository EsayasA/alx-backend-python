#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum as float"""
    e: float = 0.0
    for j in input_list:
        e += j
    return e
