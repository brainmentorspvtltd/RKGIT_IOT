import math
#num = 100000007
num = 997

if num % 2 == 0 or num % 3 == 0:
    print("Not Prime")

count = 0
for i in range(5,int(math.sqrt(num)), 6):
    count += 1
    if num % i == 0 or num % (i+2) == 0:
        print("Not Prime...")
        break
else:
    print("Prime...")

print(f"Took {count} iterations")
