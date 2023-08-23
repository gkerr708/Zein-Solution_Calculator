import datetime, csv, numpy as np

print('''
Zein solution calculator
''')

data_file = "log.csv"

def append_data(file_path, values):
    with open(file_path, 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(values)

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
    print(f"\nMass of zein is {round(abs_wgt_zein,5)} g")
    measured_wgt_zein = float(input("\nMeasured mass of zein (g): "))
    error = abs(measured_wgt_zein - abs_wgt_zein) / abs_wgt_zein 

    save_bool = input("\nDo you want to save data? (y/n): ")
    if save_bool == "y":
        purpose = input("\nWhat are the solutions for: ")
        now = datetime.datetime.now()
        time = now.strftime("%Y-%m-%d %H:%M")
        row =  [time, \
                f"{np.round(pct_wgt_zein*100,   2)}%", \
                f"{np.round(pct_vol_ethanol*100,2)}%", \
                np.round(abs_vol_ethanol,       4), \
                np.round(abs_vol_water,         4), \
                np.round(abs_wgt_zein,          4), \
                np.round(measured_wgt_zein,     4), \
                f"{np.round(error*100,          2)}%", \
                purpose]
        append_data(data_file, row)

    bool = input("\nDo you want to continue? (y/n): ")
    if bool == "n":
        break



