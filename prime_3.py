import math
num = 100000007
count = 0
for i in range(2,int(math.sqrt(num))):
    count += 1
    if num % i == 0:
        print("Not Prime...")
        break
else:
    print("Prime...")

print(f"Took {count} iterations")
