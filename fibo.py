def Fibonacci_series(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return (Fibonacci_series(n - 2)+ Fibonacci_series(n - 1))
        
n = int(input('Please Enter the Range Number: '))

for Num in range(0, n):
	print(Fibonacci_series(Num))


#Python example to find Factors of a Number

n = int(input('Enter Number: '))
value = 1
print("Factors of a Given Number {0} are:".format(n))

while (value <= n):
    if(n % value == 0):
        print("{0}".format(value))
    value = value + 1

#factorial number program

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact
num = int(input(" Please enter any Number to find factorial : "))
print(factorial(num))

