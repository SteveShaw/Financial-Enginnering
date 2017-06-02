# -*- coding: utf-8 -*-
"""
Created on Wed May 31 23:26:15 2017

@author: SteveShaw
"""

import numpy as np
import BondPricing
import scipy.optimize as sci_op

#N=14 #(from t=0 to t=N)

def RoundLattice(lattice, ndec=3):
    round_lattice = []
    for level in lattice:
        round_lattice.append(np.around(level, decimals=ndec))
    return round_lattice
    
def GenBDTShortRateLattice(a_guess, b, nper):
    lattice = [np.array(a_guess[0])]
    
    for i in range(nper):
        t = i + 1
        v = np.arange(0, t+1) * b
        v_guess= np.ones(t+1)*a_guess[t]
        v = np.exp(v)
        #lattice.append(v*a_guess)
        lattice.append(v*v_guess)
    
    return lattice

def GetZCBPrice( lattice ):
    zcb_prcs = []
    for level in lattice:
       zcb_prcs.append(np.sum(level))
    return np.array(zcb_prcs)

def GenExponents( nper ): #generate 1, 1/2, 1/3, 1/4
    exps = np.arange(0, nper+1)
    exps[0] = 1 # to avoid divide by zero for the first element
    return 1.0/exps

def LSEObjective(va, spot_rates, b, nper, exponents):
    r_lattice = GenBDTShortRateLattice(va, b, nper)
    elem_price_lattice = BondPricing.ElementaryPrices(r_lattice, nper)
    v_zcb = GetZCBPrice(elem_price_lattice)
    spot_rates_guess = np.power(1.0/v_zcb, exponents) - 1.0
    return spot_rates - spot_rates_guess #this difference will be used in sum(diff^2) in the solver
    
#using least-square to find the solution
#spot_rates: observed market spot short rates
def CalibSpotRatesByLSQ( a_guess, spot_rates, b, nper):
    exponents = GenExponents( nper )
    solution = sci_op.leastsq( LSEObjective, a_guess, 
                              args=(spot_rates, b, nper, exponents),
                                full_output=1)
    #err = np.sum(np.square(spot_rates-solution)
    #print('err=%f'%err)
    return solution

#a_guess= np.ones(N+1)*0.05
#spot_rates = np.array([0, 7.3, 7.62, 8.1, 8.45, 9.2, 
#                       9.64, 10.12, 10.45,10.75, 11.22, 
#                       11.55,11.92, 12.2, 12.32])
#                       
#spot_rates = spot_rates/100.0                       
#
#a_sol = CalibSpotRatesByLSQ( a_guess, spot_rates, 0.01, N )
#print(a_sol)

#test_vr = GenBDTShortRateLattice(a_guess, 0.01, N)
#eps = BondPricing.ElementaryPrices(test_vr,N)
##eps = RoundLattice(eps)        
#zcbs = GetZCBPrice(eps)
#vexp = GenExponents(N)
#exponents[0] = 1
#exponents = 1.0/exponents
#rates_guess = np.power(1.0/zcbs, vexp)
#print_rates_guess = (rates_guess - 1)*100.0


    
#sci_op.leastsq()