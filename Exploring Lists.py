#list functions
#take list as user input
list1 = list(map(int, input("Enter the list: ").split(',')))
#all will reutrn true if all the elements are true
print(all([1, ' ', 3, 4]))
print(all([1, True, False, ' ']))
"""any will return true even if a value is false, but it will return false only if all the values are false"""
print(any([False, False, True]))
print(any([False, False, False]))
print('enumerate:', list(enumerate(list1)))#enumerate will return the index and the element
print('max:', max(list1))#max will return the maximum element
print('min:', min(list1))#min will return the minimum element
print('length:', len(list1))#len will return the length of the list
print("sum:", sum(list1))#sum will return the sum of the elements
print("sorted:", sorted(list1))#sorted will return the sorted list

#list methods
list1 = [2,3,5,7]
list2 = [3, 11]
(list1.extend(list2))#extend will add the elements of the list at the end of the list
print(list1)
(list1.append(list2))#append will add the list as an element at the end of the list
print(list1)
print(list1.count(3))#count will return the number of times the element is present in the list
print(list1.index(3))#index will return the index of the element
list1.insert(1, 4)#insert will insert the element at the given index 1 is the index and 4 is the element
print(list1)
list3 = list1.copy()#copy will copy the list
print(list3)
list1.pop(1)#pop will remove the element at the given index
print(list1)
list1.remove(3)#remove will remove the first occurence of the element
print(list1)
list1.reverse()#reverse will reverse the list
print(list1)
list1.sort()#sort will sort the list
print(list1)
list1.clear()#clear will clear the list
print(list1)
