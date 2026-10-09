# -*- coding: utf-8 -*-


from .timegrid import Timegrid

import numpy
from dataclasses import dataclass


@dataclass(frozen = True)
class Sample(object):

    ''' Result type for a monte carlo simulation. '''
    
    grid: TimeGrid
    sims: numpy.ndarray

    # Notes
    #
    # We can fully define a simulation period by the values
    # realized, `sims`, and the corresponding timegrid, `grid`.

    @property
    def mean(self):
        return self.sims.mean(axis = 0)

    @property
    def variance(self):
        return self.sims.var(axis = 0)
