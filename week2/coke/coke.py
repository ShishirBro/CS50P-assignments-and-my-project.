Amount_Due = 50
c=0
d=0

#a=int(input("Insert coin: "))
while c<Amount_Due:
    print(f"Amount Due: {Amount_Due - c}")
    a=int(input("Insert coin: "))
    if a in [25,10,5]:
        c+=a
    else:

        print("Amount Due: ",50)
if c>=Amount_Due:
    d=c-Amount_Due
print("Change Owed:",d)





