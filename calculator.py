val1 = input("Please enter your first number:")
val2 = input("Please enter your second number:")
val3 = input("what would operation would you like to perform?:")

x = int(val1)
y = int(val2)
operation = val3

if val3 == "+" or val3 == "add":
    result = x + y
    print(f"the result is: {result}")
elif val3 == "-" or val3 == "subtract":
    result = x - y
    print(f"the result is: {result}")
elif val3 == "*" or val3 == "multiply":
    result = x * y
    print(f"the result is: {result}")
elif val3 == "/" or val3 == "divide":
    result = x / y
    print(f"the result is: {result}")
else:
    print("Sorry, I don't know how to do anything :(")

# Need to add other operations