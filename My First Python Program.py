Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
message = "Hello! How are you"
print
<built-in function print>
(
print(message)
Hello! How are you
num1 = 10
num2 = 20
sum1 = num1+num2
print(sum1)
30
#floating points
pi = 3.14
radius = 4
print('calculate the area of circle')
calculate the area of circle
print('calculating the area of circle')
calculating the area of circle
print('Calculating the area of circle')
Calculating the area of circle
area = pi*4*4
print('area=')
area=

print(area)
50.24
print('area = ' , area)
area =  50.24
#in print statement, seperate string and variable
name = 'Ajay'
print ('My name is : name')
My name is : name
print ('My name is : , name')
       
SyntaxError: incomplete input
print('My name is: ' , name)
       
My name is:  Ajay
print('The author of "Wings of Fire"')
 #Data Types In Python
 #Number ; Int Float and Complex
 a = 10
       print(type(a))
       <class 'int'>
       b = 12.343
       print(type(b))
       <class 'float'>
       c = 4+5j
       print(type(c))
       <class 'complex'>
       #strings
       str1 = 'Hello'
       str2 = "Hello"
       str3 = """ Triple quotes are used for multilines """
       print(str3)
       
       
The author of "Wings of Fire"
print("The author of 'Wings Of Fire'")
       
The author of 'Wings Of Fire'

""" This is an example of multiline comment"""
       
' This is an example of multiline comment'
import keywlord
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    import keywlord
ModuleNotFoundError: No module named 'keywlord'
import keyword
print(keyword.iskeyword("true"))
False
print
<built-in function print>
(
print(keyword.iskeyword("True"))
True
print(keyword.iskeyword("def"))
True
>>> #String Concatenation
>>> word1 = "Baked"
>>> word2 = "Bread"
>>> print(word1 + word2)
BakedBread
>>> mes = "The age of the student is "
>>> age = 18
>>> print(mes+age) #will give error here
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(mes+age) #will give error here
TypeError: can only concatenate str (not "int") to str
>>> #Below will covert age into string and concatenate
>>> print(mes + str(age))
The age of the student is 18
>>> #concatenating numbers
>>> a = "100"
>>> b = "200"
>>> print(a+b)
100200
>>> print(a + b)
100200
>>> 1 mile=5280 feet
SyntaxError: invalid syntax
>>> Mile = 5280
>>> print( 13 * Mile)
68640
>>> Hour = 60
>>> print(7 * Hour)
420
>>> Minutes = 60
>>> print(420 * 60)
25200
>>> print( 25200 + 37)
25237
