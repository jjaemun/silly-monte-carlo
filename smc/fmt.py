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
            
            (v, _) = args
            return f'Expected positive integer, got {v!r}.'
