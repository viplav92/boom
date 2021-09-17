#Python program to find Positive or Negative number
def pos_neg(n):
	if n>0:
		print('{} is +ve number'.format(n))

	else:
		print('{} is -ve number'.format(n))
	return ''
n=int(input('enter the n: '))
print(pos_neg(n))
