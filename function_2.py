# Required/Positional arguments
# def calc(x,y):
#     z = x + y
#     print("Sum is",z)

# calc(5,5)

# Keyword arguments
# calc(x=5,y =6)
# calc(y=6, x=5)

# Default arguments
def calc(x=0,y=0):
    z = x + y
    print("Sum is",z)

calc(5,6)
calc()
calc(6)
calc(x=5,y =6)
calc(y=6)
