import sys
def count_lines_of_code(filename):
    try:
        with open(filename, 'r') as file:
            lines=file.readlines()
            code_lines = 0
            in_multiline_comment = False

            for line in lines:
                line=line.strip()

                if not line or line.startswith('#'):
                    continue
                if line.startswith('"""') or line.startswith("'''"):
                    in_multiline_comment = not in_multiline_comment
                    continue
                code_lines +=1
            return code_lines
    except FileNotFoundError:
        print("File not found.")
        sys.exit(1)
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Too few command-line arguments.")
        sys.exit(1)
    if len(sys.argv)>2:
        print("Too many command-line arguments.")
        sys.exit(1)
    filename = sys.argv[1]
    if not filename.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)
    try:
        lines_of_code = count_lines_of_code(filename)
        print(lines_of_code)
    except FileNotFoundError:
        print("File does not exist.")
        sys.exit(1)
    

