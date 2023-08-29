## Script to visualize Hunt's shotgun damage

# Import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Google Sheet
sheet_id = '1zDD-zOqh_ZAO3P1PYzCLfk1Ze4vClYjsM_zpD_gqJMA'
sheet_name = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
full_table = pd.read_csv(url) # Import spreadsheet into Pandas Dataframe
full_table.drop(full_table.columns[[12,13,14]],axis=1, inplace=True) # Drop useless columns

# Determine index rows
buckshot_rows = list(np.arange(0,14,1))
pennyshot_rows = list(np.arange(15,27,1))
penny_buck_rows = list(np.arange(28,39,1))

# Create and clean up separate tables
full_table = full_table.rename(columns={"BuckShot":"Weapon"})
full_table.set_index('Weapon',inplace=True)
for i in list(full_table): full_table[i] = full_table[i].str.replace('%', '')
for i in list(full_table): full_table[i] = full_table[i].astype(float)
buckshot_table = full_table.iloc[buckshot_rows,:]
buckshot_table_trans = buckshot_table.transpose()
pennyshot_table = full_table.iloc[pennyshot_rows,:]
pennyshot_table_trans = pennyshot_table.transpose()
penny_buck_table = full_table.iloc[penny_buck_rows,:]

#print(buckshot_table.dtypes)

# Create plot for "Buckshot's Ability to One Shot Kill"
bs_yticks = list(np.arange(0,110,10))
bs_xticks = list(np.arange(0,len(list(buckshot_table)),1))
buckshot_table_trans.plot.line(
    xlabel="Distance", ylabel="Chance in %", xticks=bs_xticks, yticks=bs_yticks,title="Buckshot's Ability to One Shot Kill"
)
plt.show()

# Create plot for "Pennyshot's Ability to One Shot Kill"
ps_yticks = list(np.arange(0,110,10))
ps_xticks = list(np.arange(0,len(list(pennyshot_table)),1))
pennyshot_table_trans.plot.line(
    xlabel="Distance", ylabel="Chance in %", xticks=ps_xticks, yticks=ps_yticks,title="Pennyshot's Ability to One Shot Kill"
)
plt.show()
print(pennyshot_table)