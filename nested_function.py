def outer():
    x = 0
    def counter():
        global x
        x += 1
        return x
    return counter

counter = outer()
print(counter())

