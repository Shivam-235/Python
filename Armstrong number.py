lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
for num in range(lower, upper+1):
    temp = num 
    sum = 0  
    a = len(str(num))
    while temp > 0:
        digit = temp % 10 # 153 % 10 = 3, 15 % 10 = 5, 1 % 10 = 1   
        sum += digit ** a
        temp //= 10 # 153 // 10 = 15, 15 // 10 = 1, 1 // 10 = 0
        if num == sum:
            print(num)
        

