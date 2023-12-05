# Understanding Lists In Python
list1 = [2, 4, 5.6, 'Hello', 45.45, 100, 99]
print('First Element', list1[0]) # this will print first element
print('Print third Element', list1[2])
      #print all the elements of a list starting  from first element
print(list1[0:])
#print three elements starting from index 2
print(list1[2:5])
#using negative indexing
print(list1[-2])
print(list1[-4:-2])
print(list1[-4:-3])
#Mutable Datatype
list1[3] = 'New Word'
print(list1)
#append
list1.append(108)
list1.append(454)
#you can also append list but it will be one element
list1.append(['a','b','c'])
print(list1)
"""Extend will add another list (merge) with existing list as individual elements"""
list2 = ['new','element','in','list2']
list1.extend(list2)
print(list1)
#set
""" Set Elements should be immutable, but set itself is mutable unordered collection """
set1 = set() #this will create empty set
print(type(set1)) #Will return set

set2 = {1, 4, 56.34, 36}
print(set2)
print(type(set2))
print(sorted(set2))

#If You create empty set using {} , a dictionary will be created
set3 = {}
print(type(set3)) #Returns dictionary

#Tuples
""" Tuples are read only lists, and are immutable"""
tuple1 = tuple() #Creating an empty tuple
print(type(tuple1)) #Returns Tuple
tuple2 = (2, 4, 2, 7)
print(tuple2)
print(type(tuple2))
#Creating a tuple with one element
tup1 = (1) #this will be an integer not tuple
print(type(tup1))
tup2 = (1, ) #this will create a tuple with one element
print(type(tup2))

#You can also create a tuple without parenthesis
tup3 = 9,4,6
print(tup3)
print(type(tup3))
#dictionaries
dict1 = {'Punjab':'Chandigarh', 'Haryana': 'Chandigarh',
         'Bihar':'Patna', 'West Bengal':'Kolkata','Uttar Pardesh':'Lucknow', 'Himachal':'Shimla',
         'Telangana':'Hyderabad'}
print(dict1['Punjab'])
print(dict1['Uttar Pardesh'])
print(dict1.get('Bihar'))
print(dict1.get('Himachal'))
a = input()
print(a)
a = '10'
b = '20'
print(a+b)
a = int(input("Enter a Number:"))
b = float(input('Enter a float:'))
print(b)
str1 = 'python'
print(tuple(str1))
list1 = ["key1","key2","key3"]
list2 = ["value1","value2","value3"]
print(list1)
print(list2)
mydict= zip(list1,list2)
myset= set(mydict)
print(sorted(myset))

def helloworld():
    print("Hello World")
    print("good morning")
    print("Have a nice day")
helloworld()









                


    
        




      
