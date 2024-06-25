def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    if not (2<= len(s) <=6):
        return False
    if len(s)<2 or not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    number_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] =='0' and not number_started:
                return False
            number_started = True
        elif number_started:
            return False
    return True
if __name__ == "__main__":

    main()


