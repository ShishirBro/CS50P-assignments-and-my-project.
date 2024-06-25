def main():
    time = input("What time is it? ")
    time_hours = convert(time)
    if 7<= time_hours <=8:
        print("breakfast time")
    elif 12<= time_hours <= 13:
        print("lunch time")
    elif 18<= time_hours <=19:
        print("dinner time")
def convert(time):
    x, y = time.split(':')
    x=int(x)
    y=int(y)
    return x+y/60
if __name__ == "__main__":
    main()

