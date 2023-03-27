# Function definition
def calc():
    # local variables
    x = 12
    global y
    y = 20
    z = x + y
    print("Sum is",z)

# Function calling
calc()
