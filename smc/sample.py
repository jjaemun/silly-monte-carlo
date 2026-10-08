# -*- coding: utf-8 -*-


import numpy


class Sample(object):

    ''' Result type for a monte carlo simulation. '''

    def __init__(self, timegrid: numpy.ndarray, 
                       sims: numpy.ndarray):
        self.timegrid = timegrid
        self.sims = sims
  
    @property
    def mean(self):
        return self.sims.mean(axis = 0)

    @property
    def variance(self):
        return self.sims.var(axis = 0)
