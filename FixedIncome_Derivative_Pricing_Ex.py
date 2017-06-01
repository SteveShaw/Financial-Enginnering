# -*- coding: utf-8 -*-
"""
Created on Sat May 27 23:08:39 2017

@author: SteveShaw
"""

import BondPricing as BP



r=0.05
u=1.1
d=0.9
N=10

forward_rates = BP.GetForwardRates(r,u,d,N)
ZCB_Prices = BP.ZeroBondPricing(forward_rates, ex=N, p=0.5)

ans_1 = ZCB_Prices
print('Problems 1: %f'%ans_1)

bp_list = BP.CouponBondPricing(forward_rates, N, 0, 100, 0.5)
fp_list = BP.BondForwardPricing(forward_rates, bp_list[4], 4, 0.5)
zcb04 = BP.ZeroBondPricing(forward_rates, 4, 0.5)

ans_2 = fp_list[0]/zcb04*100
print('Problems 2: %f'%ans_2)

future_prc_list = BP.BondForwardPricing(forward_rates, bp_list[4], 4, 0.5, True)
ans_3 = future_prc_list[0]
print('Problem 3: %f'%ans_3)

opt_prcs = BP.BondOptionPricing(bond_prcs=bp_list, rates=forward_rates, strike=80, expire=6, opt_type=1, European=False, p=0.5 )
ans_4 = opt_prcs[0]
print('Problem 4: %f'%ans_4)

combined_forward_rates = BP.GetCombinedForwardRates(r,u,d,11)
eps = BP.ElementaryPrices(combined_forward_rates, 11)
V = BP.ForwardSwapPrcingUsingEP(eps, combined_forward_rates, 0.045, 1, 11)
#V = V*(10^6)
print('Problem 5: %f'%(V*1000000))