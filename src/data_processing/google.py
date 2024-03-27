import os
import pandas as pd


# Read and process Google data
def read_google_data(script_dir):
    g_data_dir = os.path.abspath(
        os.path.join(script_dir, "data", "processed", "Google")
    )
    g_dataset_path = os.path.join(g_data_dir, "Google_MD_Piedmont.csv")
    g_data = pd.read_csv(g_dataset_path, parse_dates=["date"], dayfirst=True)
    g_data.drop(
        [
            "sub_region_1",
            "grocery_and_pharmacy_percent_change_from_baseline",
            "parks_percent_change_from_baseline",
            "residential_percent_change_from_baseline",
        ],
        axis=1,
        inplace=True,
    )
    g_data.rename(
        columns={
            "transit_stations_percent_change_from_baseline": "Google_transit_stations",
            "retail_and_recreation_percent_change_from_baseline": "Google_shopping",
            "workplaces_percent_change_from_baseline": "Google_offices",
        },
        inplace=True,
    )
    g_data[
        [
            "Google_transit_stations_rolling",
            "Google_shopping_rolling",
            "Google_offices_rolling",
        ]
    ] = (
        g_data[["Google_transit_stations", "Google_shopping", "Google_offices"]]
        .rolling(7)
        .mean()
    )
    return g_data
