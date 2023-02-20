Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.reset()
for i in range(4):
    print(i)

    
0
1
2
3
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(80):
    t.forward(5*i)
    t.left(45)

    
t.reset()
t.speed(0)
for i in range(80):
    t.forward(5*i)
    t.left(45)

    
t.reset()
t.speed(0)
for i in range(80):
...     t.circle(3*i)
...     t.left(90)
... 
...     
>>> t.reset()
>>> t.color('red')
>>> t.forward(300)
>>> t.reset()
>>> colors = ['red','blue','green','orange']
>>> import random
>>> t.speed(0)
>>> for i in range(80):
...     t.color(random.choice(colors))
...     t.circle(3*i)
...     t.left(90)
... 
...     
