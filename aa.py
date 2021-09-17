l=[10,20,30,40]
i=0
n=len(l)
while i<n:
	print('current index value',i)
	print('current n value',n)
	print('remove element',l.pop(i))
	print()
	if len(l)==0:
		break
print(l)