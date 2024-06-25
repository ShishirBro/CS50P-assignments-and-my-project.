import re
def main():
    a=input("Hours: ")
    b= convert(a)
    print(b)
def convert(s):
    match = re.match(r'(\d{1,2})(?::(\d{2}))?\s(AM|PM)\s*to\s* (\d{1,2})(?::(\d{2}))?\s(AM|PM)',s)
    if match:
        start_hour = int(match.group(1))
        start_minute = int(match.group(2) or 0)
        start_period = match.group(3)
        end_hour=int(match.group(4))
        end_minute =int(match.group(5) or 0)
        end_period =match.group(6)

        if (start_hour < 1 or start_hour >12 or start_minute <0 or start_minute>59 or end_hour<1 or end_hour>12 or end_minute<0 or end_minute >59):
            raise ValueError("invalid time format")
        if start_period == 'AM':
            if start_hour ==12:
                start_hour = 0
        else:
            if start_hour!=12:
                start_hour+=12
        if end_period =='AM':
            if end_hour ==12:
                end_hour = 0
        else:
            if end_hour!=12:
                end_hour+=12
        return f"{start_hour:02d}:{start_minute:02d} to {end_hour:02d}:{end_minute:02d}"
    else:
        raise ValueError("Invalid time format")
if __name__ == "__main__":
    main()
