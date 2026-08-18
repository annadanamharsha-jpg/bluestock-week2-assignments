import requests
import pandas as pd

# Public API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check whether request was successful
if response.status_code == 200:

    # Convert JSON response into Python data
    data = response.json()

    # Convert JSON data into DataFrame
    df = pd.DataFrame(data)

    # Select useful columns
    df = df[["id", "name", "username", "email", "phone", "website"]]

    # Save as CSV
    df.to_csv("users.csv", index=False)

    print("API data successfully converted to CSV!")
    print(df)

else:
    print("API request failed.")
    print("Status code:", response.status_code)