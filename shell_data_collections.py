Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = str()
x
''
x = ''
x = list()
x
[]
x = []
text = "hello how are you ??"
len(text)
20
text[-1]
'?'
text[6]
'h'
text[0:7]
'hello h'
text[5:]
' how are you ??'
text[:5]    # start index will be 0
'hello'
text[5:]    # will return till last character
' how are you ??'
text[:]     # will return complete text
'hello how are you ??'
text[0:20]
'hello how are you ??'
text[0:20:1]
'hello how are you ??'
text[0:20:2]
'hlohwaeyu?'
text[::2]
'hlohwaeyu?'
text[0:10]
'hello how '
text[10:0]
''
text[10:0:-1]
'a woh olle'
text[-1:-10]
''
text[-1:-10:-1]
'?? uoy er'
text[::-1]  # reverse the complete string
'?? uoy era woh olleh'
dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
len(dir(str))
80
text
'hello how are you ??'
text.isalpha()
False
text.islower()
True
\
text.isupper()
False
text.upper()
'HELLO HOW ARE YOU ??'
text.lower()
'hello how are you ??'
text.capitalize()
'Hello how are you ??'
text.title()
'Hello How Are You ??'
text.swapcase()
'HELLO HOW ARE YOU ??'
text.count('o')
3
text.index('o')
4
text.index('o',0)
4
text.index('o',4)
4
text.index('o',5)
7
text.index('o',8)
15
text.index('o',16)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    text.index('o',16)
ValueError: substring not found
text.find('o')
4
text.find('o',5)
7
text.find('o',16)
-1
text.rfind('o')
15
text
'hello how are you ??'
text.split()
['hello', 'how', 'are', 'you', '??']
text = "###hello%%%"
text = "   ###hello%%%  "
text.strip()
'###hello%%%'
text = text.strip()
text
'###hello%%%'
text.lstrip('#')
'hello%%%'
text = text.lstrip('#')
text
'hello%%%'
text = text.rstrip('%')
text
'hello'
text.replace('e','p')
'hpllo'
text.encode()
b'hello'
text.startswith('a')
False
text.endswith('.')
False


data = []
dir(data)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
data.append(5)
data
[5]
data.append(15)
data
[5, 15]
data.append(7)
data
[5, 15, 7]
data.append(7,3,6,8,1)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    data.append(7,3,6,8,1)
TypeError: list.append() takes exactly one argument (5 given)
data.append([7,3,6,8,1])
data
[5, 15, 7, [7, 3, 6, 8, 1]]
del data[-1]
data
[5, 15, 7]
data.extend([7,3,6,8,1])
data
[5, 15, 7, 7, 3, 6, 8, 1]
data.insert(3,11)
data
[5, 15, 7, 11, 7, 3, 6, 8, 1]
data[2] = 12
data
[5, 15, 12, 11, 7, 3, 6, 8, 1]
data.pop()
1
data
[5, 15, 12, 11, 7, 3, 6, 8]
data.pop(4)
7
data
[5, 15, 12, 11, 3, 6, 8]
data.remove(2)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    data.remove(2)
ValueError: list.remove(x): x not in list
data.remove(3)
data
[5, 15, 12, 11, 6, 8]
data.sort()
data
[5, 6, 8, 11, 12, 15]
data.sort(reverse=True)
data
[15, 12, 11, 8, 6, 5]
data = 4
data = 4,
type(datas)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    type(datas)
NameError: name 'datas' is not defined. Did you mean: 'data'?
type(data)
<class 'tuple'>
data
(4,)
data = 4,3,54,7,8
data = (4,3,54,7,8)
data
(4, 3, 54, 7, 8)
del data[0]
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
data[0] = 10
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    data[0] = 10
TypeError: 'tuple' object does not support item assignment



data = []
for i in range(1,51):
    if i % 2 == 0:
        data.append(i)

        
data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
data = [i for i in range(1,11)]
data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data = [i**3 for i in range(1,11)]
data
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
data = [i for i in range(1,11) if i % 2 == 0]
data
[2, 4, 6, 8, 10]
data = [(i,j) for i in range(5) for j in range(5) if i != j]
data
[(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3)]
data = (i for i in range(1,11))
data
<generator object <genexpr> at 0x0000028A5FA8E7A0>



data = {}
type(data)
<class 'dict'>
data = {'name':'John','age':40,'salary':50000}
data[0]
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    data[0]
KeyError: 0
data['name']
'John'
data['age']
40
data['salary']
50000
data['name'] = 'Max'
data
{'name': 'Max', 'age': 40, 'salary': 50000}
data['dept'] = "IT"
data
{'name': 'Max', 'age': 40, 'salary': 50000, 'dept': 'IT'}
data.keys()
dict_keys(['name', 'age', 'salary', 'dept'])
data.values()
dict_values(['Max', 40, 50000, 'IT'])
data.items()
dict_items([('name', 'Max'), ('age', 40), ('salary', 50000), ('dept', 'IT')])
data["phone"]
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    data["phone"]
KeyError: 'phone'
data.get("name")
'Max'
data.get("phone")
data.get("phone", "Key not available")
'Key not available'
data.get("name", "Key not available")
'Max'
data.setdefault('address')
data
{'name': 'Max', 'age': 40, 'salary': 50000, 'dept': 'IT', 'address': None}
data['address'] = 'Delhi'
data
{'name': 'Max', 'age': 40, 'salary': 50000, 'dept': 'IT', 'address': 'Delhi'}
for i in data:
    print(i)

    
name
age
salary
dept
address
for i in data:
    print(data[i])

    
Max
40
50000
IT
Delhi
for i in data:
    print(i,":",data[i])

    
name : Max
age : 40
salary : 50000
dept : IT
address : Delhi
data = [3,4,6,12,56]
for i in range(len(data)):
    print(data[i])

...     
3
4
6
12
56
>>> for i in data:
...     print(i)
... 
...     
3
4
6
12
56
