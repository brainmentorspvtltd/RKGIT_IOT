num = 49
prime = True

for i in range(2,num):
    if num % i == 0:
        #print("Not Prime...")
        prime = False
        break

if prime:
    print("Prime Number")
else:
    print("Not Prime")
