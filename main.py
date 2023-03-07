print('''
Zein solution calculator
''')
save_folder = r""
while True:
    pct_wgt_zein = float(input("\n% weight zein: "))/100
    pct_vol_ethanol = float(input("\n% volume ethanol: "))/100
    abs_vol_solvent = float(input("\nvolume solvent (ml): "))

    density_ethanol = 0.7892  # g/ml
    density_water = 1.0 # g/ml 

    abs_vol_ethanol = abs_vol_solvent * pct_vol_ethanol 
    abs_vol_water = abs_vol_solvent - abs_vol_ethanol

    abs_wgt_ethanol = abs_vol_ethanol * density_ethanol
    abs_wgt_water = abs_vol_water * density_water
    abs_wgt_solvent = abs_wgt_ethanol + abs_wgt_water

    abs_wgt_zein = pct_wgt_zein * abs_wgt_solvent / (1 - pct_wgt_zein)

    print(f"\nVol. Ethanol: {round(abs_vol_ethanol,2)} ml, Vol. Water: {round(abs_vol_water,2)} ml")
    print(f"\nMass of zein is {round(abs_wgt_zein,5)} g\n")

    bool = input("\nDo you want to continue? (y/n): ")
    if bool == "n":
        break




