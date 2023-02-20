num = 997
count = 0
for i in range(2,num):
    count += 1
    if num % i == 0:
        print("Not Prime...")
        break
else:
    print("Prime...")

print(f"Took {count} iterations")
