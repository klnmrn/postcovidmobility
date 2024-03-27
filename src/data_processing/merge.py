"""
merge.py

Description: A script to merge mobility data.

Author: Marina Klanjcic
Date: 2024-03-27
"""

import pandas as pd


# Join 3 datasets in 1
def merge_data(fb_data, g_data, a_data):
    data = a_data.merge(g_data, on="date", how="outer").merge(
        fb_data, on="date", how="outer"
    )
    data = data.iloc[13:, :]
    return data
