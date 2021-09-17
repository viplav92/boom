#Python program to find Largest of 2 Numbers
def larger_2_num(a,b):
	if a>b:
		
		print('a is greater')
	else:
		print('b is greater')

a,b=input('enter the value of a & b: ').split()
print(larger_2_num(a,b))
#/////////////////////////////////////////////////////////////


#Python program to find Largest of 3 Numbers

def larger_2_num(a,b,c):
	if a>b and a>c:
		print('a is greater')
	elif b>a and b>c:
		print('b is greater')
	else:
		print('c is greater')

a,b,c=input('enter the value of a,b & c: ').split()
print(larger_2_num(a,b,c))