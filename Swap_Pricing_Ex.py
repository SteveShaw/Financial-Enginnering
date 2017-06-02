# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 15:09:01 2017

@author: jshao
"""

import BondPricing as BP
import Calibrate_Bond_Price as CBP
import numpy as np


a_guess= np.ones(N+1)*0.05
spot_rates = np.array([0, 7.3, 7.62, 8.1, 8.45, 9.2, 
                       9.64, 10.12, 10.45,10.75, 11.22, 
                       11.55,11.92, 12.2, 12.32])
                       
spot_rates = spot_rates/100.0                       

a_sol = CBP.CalibSpotRatesByLSQ( a_guess, spot_rates, 0.01, N )
print(a_sol)

r = 0.06
u = 1.25
d = 0.9
N = 5


#prices = []

rates = np.array([15.89, 15.82, 15.74, 15.66, 15.58, 15.50, 15.42, 15.35, 15.27, 15.20])
rates = rates/100.0
rates = np.repeat(rates, 2)
rates = np.delete(rates, 0)
rates = np.delete(rates, -1)

rates_1 = np.array([13.45, 13.38, 13.31])
prc = (rates - 0.1165)/(1.0+rates)
nrows = round(prc.shape[0]/2)
prc = np.reshape(prc, (nrows, 2))
avg_prc = np.average(prc, axis=1, weights=[0.5,0.5])


#swap_price = (rate_lattice[-1] - 0.05)/(1+rate_lattice[-1])
#prices.insert(0, swap_price)
#
#
#nrows = round(swap_price.shape[0]/2)
#swap_price = np.reshape(swap_price, (nrows, 2))
#w_prc = np.average(swap_price, axis=1, weights=[0.5,0.5])
#swap_price = ( w_prc + (rate_lattice[-2] - 0.05) ) / ( 1. + rate_lattice[-2] )
#prices.insert(0, swap_price)


