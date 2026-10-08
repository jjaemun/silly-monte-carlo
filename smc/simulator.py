# -*- coding: utf-8 -*-


import abc


class Simulator(abc.ABC):

    ''' Abstract base class for monte carlo 
            sde simulations.'''

    def __init__(self, timesteps: int, paths: int):
        assert isinstance(timesteps, int) and timesteps > 0
        assert isinstance(paths, int) and paths > 0

        self.timesteps = timesteps
        self.paths = paths


    @abc.abstractmethod
    def simulate(self, s: float, t: float) -> ...:

        ''' Computes synthetic paths over simulation 
                period [s, t].'''

        raise NotImplementedError


    @abc.abstractmethod
    def mean(self, s: float, t: float) -> ...:

        ''' Computes theoretic path of one-time first order 
                moments over the period [s, t]. '''

        raise NotImplementedError


    @abc.abstractmethod
    def variance(self, s: float, t: float) -> ...:

        ''' Returns theoretic dispersion over the 
                period  [s, t].'''

        raise NotImplementedError


    @abc.abstractmethod
    def autocovariance(self, s: float, t: float) -> ...:

        ''' Returns theoretic mixed second order central  
                moments on times s, t. '''

        raise NotImplementedError
