# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 16:52:59 2017

@author: jshao
"""

import BondPricing as BP
import Calibrate_Bond_Price as CBP
import numpy as np
import math

N = 10
b = 0.05
fr = 3.9/100.0
multiplier = math.pow(10, 6)
a_guess= np.ones(N+1)*0.03
spot_rates = np.array([0, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.55, 3.6, 3.65, 3.7])
spot_rates = spot_rates/100.0                       

#problem 1
a_sol = CBP.CalibSpotRatesByLSQ( a_guess, spot_rates, b, N )
rate_lattice = CBP.GenBDTShortRateLattice( a_sol[0], b, N )
prc_lt = BP.PricingSwaptionWithCombinedRates(rate_lattice, 3, 7, fr, 0, 1)
print('Solution 1 = %f'%(prc_lt[0]*multiplier))

#problem 2: b = 0.1
b = 0.1
a_sol = CBP.CalibSpotRatesByLSQ( a_guess, spot_rates, b, N )
rate_lattice = CBP.GenBDTShortRateLattice( a_sol[0], b, N )
prc_lt = BP.PricingSwaptionWithCombinedRates(rate_lattice, 3, 7, fr, 0, 1)
print('Solution 2 = %f'%(prc_lt[0]*multiplier))


