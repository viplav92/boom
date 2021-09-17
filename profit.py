#Python program to find Profit Or Loss

def profit_loss(cp,sp):
	if cp<sp:
		print('profit')
	else:
		print('loss')
	return ''
cp=int(input('enter the cp: '))
sp=int(input('enter the sp: '))
print(profit_loss(cp,sp))

#Python program to find Square of a Number

def square(n):
	return n*n
n=int(input('enter the value of n: '))
print(square(n))

