import re
def main ():
    a=input("Text: ")
    b=count(a)
    print(b)
def count(s):
    find=re.findall(r'\bum\b',s,re.IGNORECASE)
    count = len(find)
    return count
if __name__ == "__main__":
    main()


