a = 21
b = 19
c = a + b
d = a / b
e = a - b
f = a * b
print(c)
print("Sum is",c)
print("Sum is %d"%c)

print("Sum of", a, "and", b, "is", c)
print("Sum of {} and {} is {}".format(a,b,c))
print("Sum of {1} and {2} is {0}".format(c,a,b))
print("Div of {} and {} is {:.2f}".format(a,b,d))

#f-strings
print(f"Sum of {a} and {b} is {c}")

#print(f"Sum is {c}\nSub is {e}")

# Multi-line print
print(f"""
1. Sum is {c}
2. Sub is {e}
3. Div is {d}
4. Mul is {f}
""")














