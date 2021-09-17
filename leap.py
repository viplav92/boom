#Python program for Leap Year

def leap_year(y):
	if ((y%400==0) or (y%4==0)) and (y%100!=0):
		print('{} is a leap year'.format(y))
		return ''
	else:
		print('not a leap year')
		return ''
y=int(input('enter a year: '))
print(leap_year(y))