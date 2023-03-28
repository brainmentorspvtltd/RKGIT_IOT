# *args - variable length argument
def sum(*x):
    # print(x)
    s = 0
    for i in x:
        s += i
    print("Sum is",s)

sum()
sum(4)
sum(4,5,7)
sum(5,2,3,65,78,4,2)


# **kwargs - keyword arguments
def person(**details):
    print(details)

# person(x=3,y=6)
person(name="Ram")
person(id=101,name="Shyam",dept="IT")

