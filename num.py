# Python Program For Armstrong Number using While Loop

n= int(input("Enter the Number to Check for Armstrong: "))
Sum = 0
Times = 0
          
temp = n
while temp > 0:
           Times = Times + 1
           temp = temp // 10

# Finding Armstrong Number
temp = n
while temp > 0:
           Reminder =temp % 10
           Sum = Sum + (Reminder ** Times)
           temp //= 10
if n == Sum:
	print(" {} is Armstrong Number".format(n))
else:
    print("is Not a Armstrong Number".format(n))