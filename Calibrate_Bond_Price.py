# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:26:15 2017

@author: SteveShaw
"""

import numpy as np
import BondPricing
import scipy.optimize as sci_op

N=15

def RoundLattice(lattice, ndec=3):
    round_lattice = []
    for level in lattice:
        round_lattice.append(np.around(level, decimals=ndec))
    return round_lattice
    
def GenBDTShortRateLattice(a_guess, b, nper):
    lattice = [np.array(a_guess)]
    
    for i in range(nper):
        t = i + 1
        v = np.arange(0, t+1) * b
        v = np.exp(v)
        lattice.append(v*a_guess)
    
    return lattice

def GetZCBPrice( lattice ):
    zcb_prcs = []
    for level in lattice:
       zcb_prcs.append(np.sum(level))
    return np.array(zcb_prcs)
#def MinLSESolver( initial, target, threshold ):
a_guess= 0.05
test_vr = GenBDTShortRateLattice(a_guess, 0.01, N-1)
eps = BondPricing.ElementaryPrices(test_vr,N-1)
#eps = RoundLattice(eps)        
zcbs = GetZCBPrice(eps)

#sci_op.leastsq()