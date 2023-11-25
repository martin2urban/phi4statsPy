import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/martin2urban/pythonProject1/master/phiSlim30cols.csv"
columns= ['PhiAcc', 'ProtId', 'PathSpecies', 'PathSpeciesTaxID']
my_types = {
    "PhiAcc": str,
#   "ProtId": str,
#   "PathSpecies": str,
#  "PathSpeciesTaxID": int,

}
phi2 = pd.read_csv(
    "phiSlim30cols.csv",
    usecols=columns,
#    dtype=my_types,
    header=0,
)
print(phi2.columns)
phi2.describe(include='all')
