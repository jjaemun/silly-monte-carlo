# -*- coding: utf-8 -*-


import typing


def positive(value: typing.Any) -> None:

    ''' Check that `value` is a positive integer. '''

    if not (isinstance(value, int) and value > 0):
        raise ValueError
