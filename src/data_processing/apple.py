"""
apple.py

Description: A script to read and process Apple mobility data.

Author: Marina Klanjcic
Date: 2024-03-27
"""

import os
import pandas as pd


# Read and process Apple data
def read_apple_data(script_dir):
    a_data_dir = os.path.abspath(os.path.join(script_dir, "data", "processed", "Apple"))
    a_dataset_path = os.path.join(a_data_dir, "Apple_MD_Piedmont_mean.csv")
    a_data = pd.read_csv(a_dataset_path, sep=";", parse_dates=["date"])
    a_data.drop(
        [
            "Unnamed: 0",
            "Day_Of_Week",
            "Piedmont_driving_mean",
            "Piedmont_walking_mean",
            "Piedmont_walking",
        ],
        axis=1,
        inplace=True,
    )
    a_data.rename(columns={"Piedmont_driving": "Apple_driving"}, inplace=True)

    # Calculate rolling averages for selected columns
    a_data["Apple_driving_rolling"] = a_data["Apple_driving"].rolling(7).mean()
    return a_data
