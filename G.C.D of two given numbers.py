n = int(input("Please enter an integer: "))
m = int(input("Please enter another integer: "))
#calculate gcd
if n > m:
    smaller = m
else:
    smaller = n
for i in range(1, smaller+1):
    if((n % i == 0) and (m % i == 0)):
        gcd = i
print("The G.C.D of", n,"and", m,"is", gcd)
