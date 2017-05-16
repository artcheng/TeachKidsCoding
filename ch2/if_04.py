t=81  #temperature is 81 degree

if t>80 :
    print 'It is hot, I will wear shorts'

# what if it is not hot?
t=75
if t>80 :
    print 'It is hot, I will wear shorts'
else:
    print 'It is not hot, I will wear long leaves shirt'

# what if it could be cold?
t=45
if t>80 :
    print 'It is hot, I will wear shorts'
elif t>60:  #means else if
    print 'It is not hot, I will wear long leaves shirt'
else:
    print 'It is cold, I will wear jacket'


#What t>80 really is? The values are either Ture or False
t=81
print t,'>80 is', t>80

t=75
print t,'>80 is', t>80

#Sometimes you need two or more questions to make decision
t=70
if t<70 and t>60 :
    print 't is between 60 and 70'

if t>70 or t<60 :
    print 't is either greater than 70 or less than 60'


#understand how True False work with and or
print True and True
print True and False
print False and False

print True or True
print True or False
print False or False

#task 1: give an integer number, let the computer decide if it is an even number or odd number


#task 2: give two integer numbers, print 'Toooooo Odds' if both are odd numbers; print 'Just Right' if one is odd and the other one is even; print 'Tooooo Even' if both are even

