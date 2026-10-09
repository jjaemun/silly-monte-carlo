# -*- coding: utf-8 -*-


from . import check


import numpy


from typing import ClassVar
from dataclasses import dataclass


@dataclass(frozen=True)
class TimeGrid:

    ''' Uniform time grid over an interval. '''

    s: float
    t: float
    timesteps: int

    def __post_init__(self):

        # Notes
        #
        # We continue asserting as postconditions that
        # timesteps is positive and s < t.

        check.positive_integer(self.timesteps)
        check.cmplt(self.s, self.t)

    @property
    def increment(self):
        return (self.t - self.s) / self.timesteps

    @property
    def values(self):
        return numpy.linspace(self.s, self.t, self.timesteps + 1)
