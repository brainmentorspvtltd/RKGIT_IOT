a = 21
b = 19

#Walrus Operator :=
#print("Sum is",c := a + b)
#print(f"Sum of {a} and {b} is {(c := a + b)}")

print(f"""
1. Sum is {(c := a + b)}
2. Sub is {(d := a - b)}
3. Div is {(e := a / b):.2f}
4. Mul is {(f := a * b)}
""")


