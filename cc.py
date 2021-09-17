#Python program to check Number Divisible by 5 and 11
def div(n):
	for i in range(1,n+1):
		if i%5==0 and i%11==0:
			print('divisible by 5 and 11: ',i)
	return ''
n=int(input('enetr the n: '))
print(div(n))		
