#Python Program to find Compound Interest


import math

p = float(input(" Please Enter the Principal Amount : "))
r = float(input(" Please Enter the Rate Of Interest   : "))
t = float(input(" Please Enter Time period in Years   : "))

ci_future = p * (math.pow((1 + r / 100), t)) 
compound_int = ci_future - p

print("Future Compound Interest for Principal Amount {0} = {1}".format(p, ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(p, compound_int))

#Python example to find Simple Interest

p = float(input(" Please Enter the Principal Amount : "))
r = float(input(" Please Enter the Rate Of Interest   : "))
t = float(input(" Please Enter Time period in Years   : "))
si=(p*r*t)/100
print('the simple interest is: ',si)


#Python program to Print Natural number 1 to N

n = int(input(" Please Enter the n : "))
for i in range(1,n):
	print(i,end='')


#Python program to print Natural Numbers in Reverse Order

n = int(input(" Please Enter the n : "))
i=n
while ( i >= 1):
    print (i, end = '  ')
    i = i - 1