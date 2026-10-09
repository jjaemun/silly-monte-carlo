# -*- coding: utf-8 -*-


import abc
from .seed import Seed


class Simulator(abc.ABC):

    ''' Abstract base class for monte carlo 
            sde simulations.'''

    @abc.abstractmethod
    def simulate(self, s: float, t: float, 
                                 seed: Seed = None) -> ...:

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
