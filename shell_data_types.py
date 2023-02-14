Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 12
y = 21
z = x + y
z
33

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is c

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Div of 21 and 19 is 1.105263157894737

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Div of 21 and 19 is 1.11

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Div of 21 and 19 is 1.11
Sum of 21 and 19 is 40

========= RESTART: D:/Trainings/RKGIT_Python/01-print.py =========
40
Sum is 40
Sum is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Sum of 21 and 19 is 40
Div of 21 and 19 is 1.11
Sum of 21 and 19 is 40

1. Sum is 40
2. Sub is 2
3. Div is 1.105263157894737
4. Mul is 399


========= RESTART: D:/Trainings/RKGIT_Python/02-walrus.py ========
Traceback (most recent call last):
  File "D:/Trainings/RKGIT_Python/02-walrus.py", line 4, in <module>
    print("Sum is",c = a + b)
TypeError: 'c' is an invalid keyword argument for print()

========= RESTART: D:/Trainings/RKGIT_Python/02-walrus.py ========
Sum is 40

========= RESTART: D:/Trainings/RKGIT_Python/02-walrus.py ========
Traceback (most recent call last):
  File "D:/Trainings/RKGIT_Python/02-walrus.py", line 7, in <module>
    print(f"Sum of {a} and {b} is {c := a + b}")
NameError: name 'c' is not defined

========= RESTART: D:/Trainings/RKGIT_Python/02-walrus.py ========
Sum of 21 and 19 is 40

========= RESTART: D:/Trainings/RKGIT_Python/02-walrus.py ========

1. Sum is 40
2. Sub is 2
3. Div is 1.105263157894737
4. Mul is 399


========= RESTART: D:/Trainings/RKGIT_Python/02-walrus.py ========

1. Sum is 40
2. Sub is 2
3. Div is 1.11
4. Mul is 399


========= RESTART: D:/Trainings/RKGIT_Python/03-input.py =========
Enter your name : Ravi
Hello : Ravi

========= RESTART: D:/Trainings/RKGIT_Python/03-input.py =========
Enter your name : Ravi
Hello : Ravi
Enter first number : 12
Enter second number : 44
Result  is : 1244
fnum
'12'
type(fnum)
<class 'str'>

========= RESTART: D:/Trainings/RKGIT_Python/03-input.py =========
Enter your name : Ravi
Hello : Ravi
Enter first number : 23
Enter second number : 33
Result  is : 56




x = 12
type(x)
<class 'int'>
x = 12,
type(x)
<class 'tuple'>
x = 4.5
type(x)
<class 'float'>
x = 3 + 5i
SyntaxError: invalid decimal literal
x = 3 + 5j
type(x)
<class 'complex'>
x = "hello"
x = 'hello'
x = """hello"""
x = '''hello'''
x = b'34'
type(x)
<class 'bytes'>
x = True
type(x)
<class 'bool'>
>>> x = [4,3,5,7]
>>> x = (3,4,6,7)
>>> x = 3,4,6,7
>>> type(x)
<class 'tuple'>
>>> x = 2,
>>> type(x)
<class 'tuple'>
>>> x = {'name' : "Ram"}
>>> x = {3,5,6,2,6,9}
>>> type(x)
<class 'set'>
