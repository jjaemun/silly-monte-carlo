# -*- coding: utf-8 -*-


from . import err, fmt
import typing


def positive_integer(obj: typing.Any) -> None:

    ''' Check that `obj` is a positive integer. '''

    if not (isinstance(obj, int) and obj > 0):
        raise ValueError(fmt.msg(err.Err.POSITIVE_INTEGER, obj))


def cmplt(lhs: float, rhs: float) -> None:

    ''' Checks that `lhs` is less than `rhs`. '''

    if (lhs > rhs):
        raise ValueError(fmt.msg(err.Err.CMPLT, lhs, rhs))
