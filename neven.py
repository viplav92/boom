#Python program to print Even Numbers from 1 to 100
def even_num(n):
	for i in range(1,n):
		if i%2==0:
			print('{} is even number'.format(i))
		else:
			print('{} is odd number'.format(i))
	return ''
print(even_num(101))