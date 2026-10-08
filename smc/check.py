# -*- coding: utf-8 -*-


from . import err, fmt
import typing


def positive_integer(any: typing.Any) -> None:

    ''' Check that `value` is a positive integer. '''

    if not (isinstance(any, int) and any > 0):
        raise ValueError(fmt.msg(err.Error.POSITIVE_INTEGER, any))
