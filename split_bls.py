# %%
import pandas as pd
import sys

YEAR = sys.argv[1]

df = pd.read_excel("data/all_data_M_{YEAR}.xlsx")


# %%
# Keep detailed records for the Data Scientists Occupational classification
df = df[(df["O_GROUP"] == "detailed") & df["OCC_TITLE"].str.contains("Data Scientist")]


# %%
df[df["AREA"] == 99].to_csv("data/bls_all_data_M_{YEAR}_industry.csv", index=False)


# %%
df[df["AREA"].between(1, 98, inclusive="both")].to_csv(
    "data/bls_all_data_M_{YEAR}_states.csv", index=False
)


# %%
df[df["AREA"].gt(99) & ~df["AREA_TITLE"].str.contains("nonmetropolitan")].to_csv(
    "data/bls_all_data_M_{YEAR}_metro.csv", index=False
)


# %%
df[df["AREA"].gt(99) & df["AREA_TITLE"].str.contains("nonmetropolitan")].to_csv(
    "data/bls_all_data_M_{YEAR}_non_metro.csv", index=False
)


# %%
