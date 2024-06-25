def main():

    a=input("Input: ")
    output = shorten(a)
    print("Output:",output)
def shorten(a):


    vowels = "aeiou"
    Output = ""
    for c in a:
        if c not in vowels:
            Output +=c
    return Output
if __name__ == "__main__":
    main()





