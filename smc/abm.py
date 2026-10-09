# -*- coding: utf-8 -*-


import numpy
from . import (check, simulator, sample, seed, timegrid)



class ArithmeticBrownianMotion(simulator.Simulator):

    ''' Arithmetic Brownian motion (abm) monte 
            carlo simulator. '''
        
    def __init__(self, spot: float, mu: float, sigma: float, 
                       timesteps: int, paths: int, seed: seed.Seed = None):
        self.spot = spot
        self.mu = mu
        self.sigma = sigma 

        # Notes
        #
        # We assert that `timesteps` and `paths` be 
        # positive integers. 

        check.positive_integer(timesteps)
        check.positive_integer(paths)

        self.timesteps = timesteps
        self.paths = paths

        # --priv.
        self._rng = numpy.random.default_rng(seed)

    def simulate(self, s: float, t: float) -> sample.Sample:

        '''  Computes synthetic paths over simulation 
                period [s, t]. '''
    
        grid = timegrid.TimeGrid(s, t, self.timesteps)
        gaussians = (numpy.sqrt(grid.increment) 
                        * self._rng.normal(size = (self.paths, self.timesteps)))
        
        drift = self.mu * grid.increment
        diffusion = self.sigma * gaussians

        ds = numpy.concatenate([numpy.full((self.paths, 1), self.spot), 
                                drift + diffusion], axis=1)

        return sample.Sample(grid = grid, 
                             sims = numpy.cumsum(ds, axis = 1))


    def mean(self, s: float, t: float) -> ...:
        
        ''' Computes theoretic path of one-time first order 
                moments over the period [s, t]. '''

        grid = timegrid.TimeGrid(s, t, self.timesteps)
        return self.spot + self.mu * (grid.values - s)


    def variance(self, s: float, t: float) -> ...: 

        ''' Returns theoretic dispersion over the 
                period  [s, t].'''

        grid = timegrid.TimeGrid(s, t, self.timesteps)
        return self.sigma * self.sigma * (grid.values - s)


    def autocovariance(self, s: float, t: float) -> ...:

        ''' Returns theoretic mixed second order central  
                moments on times s, t. '''

        return self.sigma * self.sigma * min(s, t)
