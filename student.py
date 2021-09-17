#This python program allows users to enter five different values for five subjects.
#Next, it finds the Total, and Percentage of those Five Subjects.
english = float(input(" Please enter English Marks: "))
math = float(input(" Please enter Math score: "))
computers = float(input(" Please enter Computer Marks: "))
physics = float(input(" Please enter Physics Marks: "))
chemistry = float(input(" Please enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
percentage = (total / 500) * 100
print('% is',percentage)
print('total mark obtained',total)