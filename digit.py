#Python program to print First Digit of a Number
num = int(input(" Please enter any Number : "))
first_digit = num

while (first_digit >= 10):
    first_digit = first_digit // 10

print("The First Digit from a Given Number {} = {} ".format(num, first_digit))