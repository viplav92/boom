#///////////////////////////////////////////////////////////////////////////////////
num1=float(input('enter the num1 value: '))
num2=float(input('enter the num2 value: '))
add = num1 + num2
sub = num1 - num2
multi = num1 * num2
div = num1 / num2
mod = num1 % num2
expo = num1 ** num2
print("The Sum of {} and {} = {}".format(num1, num2, add))
print("The Subtraction of {} from {} = {}".format(num2, num1, sub))
print("The Multiplication of {} and {} = {}".format(num1, num2, multi))
print("The Division of {} and {} = {}".format(num1, num2, div))
print("The Modulus of {} and {} = {}".format(num1, num2, mod))
print("The Exponent Value of {} and {} = {}".format(num1, num2, expo))
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def sum(num1,num2):
	add = num1 + num2
	return add
def sub(num1,num2):
	sub = num1 - num2
	return sub
def mul(num1,num2):
	multi = num1 * num2
	return multi
def div(num1,num2):
	div = num1 / num2
	return div
def mod(num1,num2):
	mod = num1 % num2
	return mod
def expo(num1,num2):
	expo = num1 ** num2
	return expo
num1=int(input('enter the num1 value: '))
num2=int(input('enter the num2 value: '))
print(sum(num1,num2))
print(sub(num1,num2))
print(mul(num1,num2))
print(div(num1,num	2))
print(mod(num1,num2))
print(expo(num1,num2))