# -*- coding: utf-8 -*-


from . import err, fmt
import typing


def positive_integer(obj: typing.Any) -> None:

    ''' Check that `value` is a positive integer. '''

    if not (isinstance(obj, int) and obj > 0):
        raise ValueError(fmt.msg(err.Err.POSITIVE_INTEGER, obj))
