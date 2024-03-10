# %%
import pandas as pd
import sys

# Command line tool for splitting the bls data-files
# If we use additional years and they have the same 
# file structure, run this by typing 
# python split_bls.py YEAR into the commandline (replacing YEAR)

YEAR = sys.argv[1]
df = pd.read_excel(f"data/all_data_M_{YEAR}.xlsx")

# Keep detailed records for the Data Scientists Occupational classification
df = df[(df["O_GROUP"] == "detailed") & df["OCC_TITLE"].str.contains("Data Scientist")]

df[df["AREA"] == 99].to_csv(f"data/bls_all_data_M_{YEAR}_industry.csv", index=False)

df[df["AREA"].between(1, 98, inclusive="both")].to_csv(
    f"data/bls_all_data_M_{YEAR}_states.csv", index=False
)

df[df["AREA"].gt(99) & ~df["AREA_TITLE"].str.contains("nonmetropolitan")].to_csv(
    f"data/bls_all_data_M_{YEAR}_metro.csv", index=False
)

df[df["AREA"].gt(99) & df["AREA_TITLE"].str.contains("nonmetropolitan")].to_csv(
    f"data/bls_all_data_M_{YEAR}_non_metro.csv", index=False
)
