def main():
    while True:
        try:
            x=input("Fraction: ")
            percentage = convert(x)
            result = gauge (percentage)
            print(result)
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
def convert(fraction):
    try:

        n,d = fraction.split('/')
        n=int(n)
        d=int(d)
    except ValueError:
        raise ValueError("Value incorrect")
    if d==0:
        raise ZeroDivisionError("denominator cannot be zero")
    if n>d:
        raise ValueError("Value incorrect")




    percentage=(n/d)*100
    return percentage
def gauge(percentage):

    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return f"{percentage:.0f}%"
if __name__ == "__main__":
      main()



