x,y,z = 10,20,30

'''
if x > y and x > z:
    print("X is greatest")
elif y > x and y > z:
    print("Y is greatest")
else:
    print("Z is greatest")
'''
output = "X" if x > y and x > z else "Y" if y > x and y > z else "Z"
print(output,"is greatest")
