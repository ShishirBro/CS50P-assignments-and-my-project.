names =[]
try:
    while True:
        name= input("Input: ")
        names.append(name)
except EOFError:
    pass
if len(names) == 1:
    print(f"\nAdieu, adieu, to {names[0]}")
elif len(names) == 2:
    print(f"\nAdieu, adieu, to {names[0]} and {names[1]}")
else:
    print(f"\nAdieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}")

