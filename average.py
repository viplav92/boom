#Python example to find Sum and Average of Natural Numbers
n = int(input(" Please Enter the n : "))
sum=0
for i in range(1,n+1):
	sum+=i
	average=sum/n
print('the sum is: ',sum)
print('the avg is: ',average)


# Python Program to find Sum of N Natural Numbers
 
number = int(input("Please Enter any Number: "))

total = 0
value = 1

while (value <= number):
    total = total + value
    value = value + 1

print("The Sum of Natural Numbers from 1 to {} =  {}".format(number, total))