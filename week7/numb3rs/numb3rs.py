import re
import sys


def main():
    a = input("IPv4 Address: ")
    result = validate(a)
    print (result)



def validate(ip):
    parts=ip.split('.')
    for part in parts:
        if (len(parts))!=4:
            return False
        if not part.isdigit():
            return False
        if not 0 <= int(part) <=255:
            return False

        return True







if __name__ == "__main__":
    main()
