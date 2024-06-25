grocery_list={}
while True:
    try:
        item=input().upper()
        if item:
            if item in grocery_list:
                grocery_list[item]+=1
            else:
                grocery_list[item]=1
    except EOFError:
        break
for key in sorted(grocery_list):
    print(f"{grocery_list[key]} {key}")

