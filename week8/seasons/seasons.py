from datetime import date
import inflect
import sys
import re

def main():
    a=input("Date of Birth: ")
    b=get_min(a)
    print(b)
def get_min(a):
    if search :=re.search(r'^(\d{4})-(\d{2})-(\d{2})$',a):
        a=list(search.groups())
    else:
        sys.exit('Invalid date')
    input_bday = convert_and_check(a)
    today = date.today()
    bday = date(input_bday[0], input_bday[1], input_bday[2])
    diff = bday - today
    no_of_days = -int(diff.days)
    minutes = no_of_days * 24 *60
    inf = inflect.engine()
    min_words = inf.number_to_words(minutes)
    min_words = min_words.replace(' and ', ' ').capitalize()
    return min_words + ' minutes'
def convert_and_check(day):
    day = list(map(int,day))
    if day[1]<0 or day[1]>12:
        sys.exit('Invalid date')
    if day[2]<0 or day[2]>31:
        sys.exit('Invalid date')
    return day
if __name__ == "__main__":
    main()

