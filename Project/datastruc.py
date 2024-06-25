import requests
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data(lat, lon, start_date, end_date):
    """Fetch precipitation data from NASA POWER API."""
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR&community=RE&longitude={lon}&latitude={lat}&start={start_date}&end={end_date}&format=JSON"
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()
    return data


def main():
    # User inputs
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    start_date = input("Enter start date (YYYYMMDD): ")
    end_date = input("Enter end date (YYYYMMDD): ")

    # Fetch data
    data = fetch_data(lat, lon, start_date, end_date)

    # Print the entire JSON response to check its structure
    print("Full API Response:")
    print(data)

    # Process data into a DataFrame
    try:
        records = data['properties']['parameter']['PRECTOTCORR']
        dates = list(records.keys())
        values = list(records.values())
        df = pd.DataFrame({'Date': dates, 'Precipitation Corrected (mm/day)': values})
        print("Data fetched successfully!")

        # Plotting
        df['Date'] = pd.to_datetime(df['Date'])
        plt.figure(figsize=(10, 5))
        plt.plot(df['Date'], df['Precipitation Corrected (mm/day)'], label='Daily Precipitation Corrected')
        plt.title('Daily Corrected Precipitation Time Series')
        plt.xlabel('Date')
        plt.ylabel('Precipitation Corrected (mm/day)')
        plt.legend()
        plt.grid(True)
        plt.savefig('precipitation_corrected_time_series.png')
        print("Plot saved as 'precipitation_corrected_time_series.png'.")

        # Saving to CSV
        df.to_csv('precipitation_corrected_data.csv', index=False)
        print("Data saved to 'precipitation_corrected_data.csv'.")

    except KeyError as e:
        print(f"KeyError: {e} - Check the JSON structure for the correct keys.")


if __name__ == "__main__":
    main()

