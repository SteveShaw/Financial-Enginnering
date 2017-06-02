# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 16:07:44 2017

@author: jshao
"""

import BondPricing as BP
import Calibrate_Bond_Price as CBP
import numpy as np


r = 0.06
u = 1.25
d = 0.9
N = 14

fr = 0.1165

a_guess= np.ones(N+1)*0.05
spot_rates = np.array([0, 7.3, 7.62, 8.1, 8.45, 9.2, 
                       9.64, 10.12, 10.45,10.75, 11.22, 
                       11.55,11.92, 12.2, 12.32])
                       
spot_rates = spot_rates/100.0                       

a_sol = CBP.CalibSpotRatesByLSQ( a_guess, spot_rates, 0.01, N )
rate_lattice = CBP.GenBDTShortRateLattice( a_sol[0], 0.01, N )

prc_lt = BP.PricingSwaptionWithCombinedRates(rate_lattice, 2, 8, 0.1165, 0, 1)

