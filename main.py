import pandas as pd

year = 2022
workbook = f"ARWU subject {year}-all subjects.xlsx"

all_dfs = pd.read_excel(workbook, sheet_name=None, index_col=0)
sheets = list(all_dfs.keys())

master = pd.DataFrame()

for i in range(len(sheets)):
    curr_key = sheets[i]
    curr = all_dfs[curr_key]

    curr["Discipline"] = curr_key
    curr["Year"] = year

    master = pd.concat([master, curr])

master.to_excel(f"{year}_stacked.xlsx", index=False)