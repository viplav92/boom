#Python Program to Count Number of Digits in a Number

n= int(input("Enter the Number for counting: "))
count = 0
while(n > 0):
    n = n // 10
    count +=  1
print('count of Digits in a Number is: {}'.format(count))
