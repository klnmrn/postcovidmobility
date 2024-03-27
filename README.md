# Post-COVID Mobility in Piedmont region in Italy
> Last modified on 2024-03-27

This repository provides the data and the code to analyze mobility behaviours in Piedmont region in Italy during and after the COVID-19 pandemic thanks to open data from Apple, Google and Facebook.

The data taken into consideration included:
- general movements from Facebook (Movement Range Maps)
- requests for travel indications by car from Apple Maps (Mobility Trends Report)
- shopping areas and entertainment venues attendances; and office attendances from Google Maps (COVID-19 Community Mobility Reports)

<img src='https://github.com/klnmrn/postcovidmobility/blob/main/reports/figures/Post-Covid_Mobility_Piedmont.png' width="1000" align="center"/>

---
## Requirements
* Python, Jupyter
* Pandas, NumPy, Matplotlib, Seaborn

## [Data](data)
The data from Apple, Google and Facebook were downloaded in 2021 when I worked on this project and when they were publicly available.

## [Python script](src/main.py)
This script performs data processing on Apple, Google and Facebook datasets and visualizes the data in one figure.<br>
**Before running the script make sure to have all the requirements installed and the data downloaded locally with path adjustment in the code.**

## Credits
I developed this work for a local Trade Union during my time at LINKS Foundation in Turin, Italy.

## Contacts
Data and code-related questions should be addressed to Marina Klanjčić (mrnkln@outlook.com).

## [MIT License](https://github.com/klnmrn/postcovidmobility/blob/main/LICENSE)

[Back To The Top](#post-COVID-Mobility)
