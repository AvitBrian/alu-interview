#!/usr/bin/python3
"""Alu-interview minimum operationss"""
import math


def minoperations(n):
    """Minimum operations"""
    if n <= 1:
        return 0
    ops = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            ops += i
            n //= i
    if n > 1:
        ops += n
    return ops
