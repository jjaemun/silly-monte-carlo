# -*- coding: utf-8 -*-


import numpy

from typing import ClassVar
from dataclasses import dataclass


@dataclass(frozen = True)
class Sample(object):

    ''' Result type for a monte carlo simulation. '''
    
    ARRAY: ClassVar = numpy.ndarray

    timegrid: ARRAY
    sims: ARRAY
 
    @property
    def mean(self) -> ARRAY:
        return self.sims.mean(axis = 0)

    @property
    def variance(self) -> ARRAY:
        return self.sims.var(axis = 0)
