#Python program for Multiplication Table

n=int(input('enetr the n: '))
print("Table of {} is".format(n))
for i in range(n,n+1):
    for j in range(1, 11):
        print('{}  *  {}  =  {}'.format(i, j, i*j))
    print()
