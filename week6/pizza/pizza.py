import sys
import csv
from tabulate import tabulate
def load_menu(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            menu = [row for row in reader]
            return menu
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
def main():
    if len(sys.argv)<2:
        print("Too few command-line arguments.")
        sys.exit(1)
    if len(sys.argv)>2:
        print("Too many command-line arguments.")
        sys.exit(1)
    filename = sys.argv[1]
    if not filename.endswith('.csv'):
        print("Not a CSV file.")
        sys.exit(1)
        
    menu = load_menu(filename)
    headers = menu[0].keys()
    table = [[row[header] for header in headers] for row in menu]
    print(tabulate(table, headers=headers, tablefmt="grid"))
if __name__ == "__main__":
    main()

