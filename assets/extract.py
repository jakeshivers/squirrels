import pandas as pd
from sodapy import Socrata
import os


# Ensure the assets directory exists
os.makedirs("assets", exist_ok=True)

if not os.path.exists("assets/data.json"):
    try:
        # Unauthenticated client only works with public data sets. Note 'None'
        # in place of application token, and no username or password:
        client = Socrata("data.cityofnewyork.us", None)

        # Example authenticated client (needed for non-public datasets):
        # client = Socrata(data.cityofnewyork.us,
        #                  MyAppToken,
        #                  username="user@example.com",
        #                  password="AFakePassword")

        # First 2000 results, returned as JSON from API / converted to Python list of
        # dictionaries by sodapy.
        results = client.get_all("vfnx-vebw")

        # Convert to pandas DataFrame
        df = pd.DataFrame.from_records(results)

        with open("assets/data.json", "w") as f:
            f.write(df.to_json())

        with open("assets/data.csv", "w", errors="ignore", newline="") as f:
            f.write(df.to_csv())
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("File already exists")
