sumfact = 0
num = int(input("Enter a number: "))
temp = num
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1,digit+1):
        fact *= i
    sumfact += fact
    temp //= 10
if num == sumfact:
    print(num,"is a strong number")
else:   
    print(num,"is not a strong number")