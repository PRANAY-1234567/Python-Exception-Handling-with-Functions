def division(x, y):
    try:
        d = x // y  # Integer division like Java
        print("Division is", d)

    except ZeroDivisionError:
        print("Error in data : Divisor should not be zero")

print("Program starts...")

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    division(a, b)

except ValueError:
    print("Error in data : Number not provided correctly")

print("Program ends...")
