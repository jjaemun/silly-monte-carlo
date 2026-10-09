# -*- coding: utf-8 -*-


import os
import enum


from typing import Union


class extension(enum.Enum):

    ''' File extensions. '''

    pdf = '.pdf'
    png = '.png'


def resolve(path: Union[str, os.PathLike]) -> bool:

    ''' Checks whether `path` exists. '''

    if not os.path.exists(path):
        ...
