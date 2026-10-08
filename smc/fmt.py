# -*- coding: utf-8 -*-


from . import err


def concat(*strings: str) -> str:

    ''' Concatenates a bunch of strings. '''

    return ''.join(strings)


def msg(e: err.Err, *args: ...) -> str:

    ''' Constructs formatted string from error code. '''
    
    args = tuple(args)

    match (e):
        case (err.Err.POSITIVE_INTEGER):

            # In the `POSITIVE_INTEGER` case, we expect to upack
            # just one value. 
            
            (v, ) = args
            return f'Expected positive integer, got {v!r}.'

        case (err.Err.CMPLT):

            # In the `CMPLT` case, we expect to unpack the two
            # values needed for the comparison operator.

            (lhs, rhs, ) = args
            return f'Requires that {lhs!r} is less than {rhs!r}.'
