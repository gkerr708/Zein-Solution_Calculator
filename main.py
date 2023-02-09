'''
Zein solution calculator
'''

pct_wgt_zein = int(input("% weight zein: "))/100
pct_vol_ethanol = int(input("% volume ethanol: "))/100
abs_vol_solvent = int(input("volume solvent (ml): "))/100

density_ethanol = 0.7892  #g/ml
density_water = 1.0 #g/ml 

abs_vol_ethanol = abs_vol_solvent * pct_vol_ethanol
abs_vol_water = abs_vol_solvent - abs_vol_ethanol

abs_wgt_ethanol = abs_vol_ethanol * density_ethanol
abs_wgt_water = abs_vol_water + density_water
abs_wgt_solvent = abs_wgt_ethanol + abs_wgt_water

pct_wgt_solvent = 1 - pct_wgt_zein
abs_wgt_zein = abs_wgt_solvent * pct_wgt_zein / pct_wgt_solvent
 
print(f"Mass of zein {abs_wgt_zein} g")




