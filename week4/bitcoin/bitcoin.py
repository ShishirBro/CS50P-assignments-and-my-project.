import sys
import requests
def fetch_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data=response.json()
        return float(data['bpi']['USD']['rate_float'])
    except requests.RequestException:
        print("Failed to retrieve Bitcoin data.")
        sys.exit(1)
def main():
    if len(sys.argv)!=2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    current_price = fetch_bitcoin_price()
    total_cost = num_bitcoins * current_price
    formatted_cost = f"${total_cost:,.4f}"
    print(formatted_cost)
if __name__ == "__main__":
    main()

