#Import Libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import compound_interface as interface
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#Import .xlsx
numtable = pd.read_excel(r'C:\Users\gamer\PycharmProjects\pythoninonehour\hunt_stuff\compound_data.xlsx')

#Functions
def exp_convert():
    exptable.armored = exptable.armored * 60
    exptable.grunt = exptable.grunt * 10
    exptable.meat_head = exptable.meat_head * 200
    exptable.hive = exptable.hive * 30
    exptable.immolator = exptable.immolator * 50
    exptable.water_devil = exptable.water_devil * 10
    exptable.hellhound = exptable.hellhound * 20

def exp_per_compound():
    exp_array = []
    for i in numtable.compound_name.unique():
        total_exp_table = exptable.query(f"compound_name==\'{i}\'")
        exp_array.append(total_exp_table['total_exp'].mean())
    return exp_array

#Manipulation
numtable = numtable.sort_values(by='compound_name')

exptable = numtable.copy()
exp_convert()
exptable['total_exp'] = exptable[:].sum(axis=1)

compoundtable = pd.DataFrame({
    "compound_name":numtable.compound_name.unique(),
    "avg_exp":exp_per_compound()
})

#Interface?
use_interface = "y"
if use_interface == "y":
    interface

#Output
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(compoundtable)

comp_plt_x = numtable.compound_name.unique()
comp_plt_y = exp_per_compound()
plt.bar(comp_plt_x,comp_plt_y)
plt.show()

# OLD SHIT -------------------------------
#path = (r'C:\Users\gamer\PycharmProjects\pythoninonehour\compound_data.xlsx')
#csv_read = pd.read_excel(path)
#csv_read = pd.DataFrame(csv_read)
#csv_read = csv_read.insert(8, "total_exp", np.arange(0, 5))