#program to print fibonacci series
# 0 1 1 2 3 5 8 13 21 34 55 89 144
n = int(input("n: "))
a = 0
b = 1
print(a)
print(b)
for i in range(2, n):
    c = a + b
    a = b
    b = c
    print(c)
#fibonacci series using recursion


    




        
