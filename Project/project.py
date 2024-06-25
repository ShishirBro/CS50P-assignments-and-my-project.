import requests
import pandas as pd
import matplotlib.pyplot as plt

def main():
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    start_date = input("Enter start date (YYYYMMDD): ")
    end_date = input("Enter end date (YYYYMMDD): ")
    data = fetch_data(lat, lon, start_date, end_date)
    df = process_data(data)
    plot_data(df)
    df.to_csv('precipitation_corrected_data.csv', index=False)
    print("Data and plot saved.")

def fetch_data(lat, lon, start_date, end_date):
    """Fetch precipitation data from NASA POWER API."""
    url = f"https://power.larc.nasa.gov/api/temporal/daily/point?parameters=PRECTOTCORR&community=RE&longitude={lon}&latitude={lat}&start={start_date}&end={end_date}&format=JSON"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_data(data):
    """Convert raw API data to a pandas DataFrame."""
    records = data['properties']['parameter']['PRECTOTCORR']
    dates = list(records.keys())
    values = list(records.values())
    df = pd.DataFrame({'Date': dates, 'Precipitation Corrected (mm/day)': values})
    return df

def plot_data(df):
    """Plot and save a time series of the precipitation data."""
    df['Date'] = pd.to_datetime(df['Date'])
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Precipitation Corrected (mm/day)'], label='Daily Precipitation Corrected')
    plt.title('Daily Corrected Precipitation Time Series')
    plt.xlabel('Date')
    plt.ylabel('Precipitation Corrected (mm/day)')
    plt.legend()
    plt.grid(True)
    plt.savefig('precipitation_corrected_time_series.png')

if __name__ == "__main__":
    main()
