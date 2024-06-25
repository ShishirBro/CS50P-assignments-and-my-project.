s=input("Enter camel case: ")
snake_case = ""
for c in s:
    if c.isupper():
        snake_case += "_" + c.lower()
    else:
        snake_case += c
print(snake_case)


