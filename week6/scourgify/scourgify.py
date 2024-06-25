import sys
import csv
def split_names(input_file, output_file):
    try:
        with open(input_file, 'r') as in_file:
            reader = csv.DictReader(in_file, fieldnames=['Name', 'house'])
            next(reader)
            fieldnames = ['first', 'last', 'house']

            with open(output_file, 'w') as out_file:
                writer = csv.DictWriter(out_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    full_name = row['Name']
                    try:

                        first_name, last_name = full_name.split(',',1)
                        writer.writerow({'first':first_name, 'last':last_name, 'house': row['house']})
                    except ValueError:
                        pass
                    
    except FileNotFoundError:
        print(f"Could not read {input_file}.")
        sys.exit(1)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Too many or few command line arguments")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    split_names(input_file, output_file)
