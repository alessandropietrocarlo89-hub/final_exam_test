import io
import requests
import pandas as pd
url = "https://esploradati.istat.it/SDMXWS/rest/data/41_983?startPeriod=2021&endPeriod=2025" 
headers = {"Accept": "application/vnd.sdmx.data+csv;version=1.0.0"}
r = requests.get(url, headers=headers)
if r.status_code == 200:
    df = pd.read_csv(io.StringIO(r.text))
    df.to_csv("istat_cars_accidents_2021_2025.csv", index=False)
    print("data saved successfully")
else:
    print(f"Failed to retrieve data. Status code: {r.status_code}")
