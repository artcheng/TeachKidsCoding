#Variable likes a tag of some value

name='Yi Cheng'
print (name)

#variable could tag to ANY type of value

# string
name='Yi Cheng'
print (name)

a='100'
print a

# number( integer )
a=100
print a

#What is the difference between string and number?
a='100'
b='200'
print 'string a+b is', a+b

a=100
b=200
print 'number a+b is', a+b

#Even for numbers, integer is different from decimal, so you have to chose the right type when you use it
a=100 #integer
print a/3

a=100.0  #decimal number
print a/3


#To change types
a='100' #string

print 'a*2 as string: ', a*2
print 'a*2, convert a to integer:', int(a)*2
print 'a/3, convert a to decimal:', float(a)/3

#task 1
#create a variable, firstname, which tags your first name (string)
#create a variable, lastname, which tags your last name (string)
#print your full name


#task 2
#fix these errors

#2.1 variable name can't have space
#full_name="Yi Cheng"   #right
#full name="Yi Cheng"   #wrong

#2.2 some words is reserved by python, they are called key words.
#print=5  #print can't be used as variable

#2.3 variables are case sentitive
#fullname="Yi Cheng"
#print Fullname     #wrong

#Note = for variable means assignment, it is different from = in math
a = 5  #assign 5 to a
print 'a is ',a

a = a + 1  #assign a+1, which is 5+1, to a .  In math x= x + 1 is totally wrong statement
print 'a is ',a

#Another thing need to be careful
a=5
b=6
c=a+b

print 'c is ',c  #what is c here?

b=7

print 'c is ', c #is c changed while b is changed?
