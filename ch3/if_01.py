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
    print 'It is not hot, I will wear jacket'


#What t>80 really is?

t=81
print t,">80 is", t>80

t=75
print t,">80 is", t>80
