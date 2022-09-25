import pandas as pd
import numpy as np
import os
"""
Generate a full csv roster out of available cafe resources
"""

def main():
    filepath = os.path.join(os.path.dirname(__file__), "capability.csv")
    data = np.array(pd.read_csv(filepath))
    print(data)
    data = get_capability_index(data)

    # print(data["Name"])

def get_capability_index(data):
    if (data[1,2] == "nan"):
        print("yes")
    return np.count_nonzero(data, axis=1)

main()
