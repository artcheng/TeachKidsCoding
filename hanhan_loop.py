# Loop Team Exercise
# Cooking involves different steps in adding the ingredients. Once you have the dough ready, you need to add
# "tomato sauce' "cheese" "pepperoni" "ham" "pepper" "spinach" "mushroom"
# use a loop function to describe this process by saying "then add"
# then use loop and index function to say, add "tomato sauce" before adding "cheeese," add "cheese" before adding "pepperoni" etc. between every step, print "let the pizza rest for 5 minutes"
# add ingredients "sausage bits" and "pineapple cubes" by using the append function
# use range function to say add "tomato sauce" and "cheese" together
# count how many ingredients are in the list by using len
# Use range function to add three ingredients together


awesome_pizza=['tomato sauce','cheese','pepperoni','ham','pepper','spinach','mushroom']
print (awesome_pizza)
for i in awesome_pizza:
    print 'then add',i
awesome_pizza.append('sausage bits')
awesome_pizza.append('pineapple cubes')
print (awesome_pizza)
n=len(awesome_pizza)
print 'there are',n,'ingredients in the pizza'
for i in range(0,n-1):
    print "add", awesome_pizza[i],"before adding", awesome_pizza[i+1]

n=len(awesome_pizza)
for i in range(0,n-1):
    print 'add', awesome_pizza[i+1],'after adding',awesome_pizza[i]


family=['Dad','Mom','Aunt','Daughters','Bannana']
print (family)
for f in family:
    print f,'loves flowers'

n=len(family) # this is counting how many items are in a list, family is the name of the list
for f in range(0,n-1): #we repeat whatever we do with each one of the items in the list
    print family[f],'is older than',family[f+1] #this is where you make sentence with the variables and strings, Strings are words that do not change. variables change, so you need to have " for strings. but you also need to indicate which list are you doing the loop function.

#loop 7
n=11
total=1
for i in range (1,n):
    total=total*i
    print "10*9*8...*1", total

#task 3: figure out the total of 1+2+3+4+5.....+200, print "the total of 1+2+3+4+5...+200 equals" xxx
#task 4: figure out the total of 1*3*5*7....*201, print "the total of 1*3*5*7...*201 equals" xxx

n=201
total=0
for i in range (1,n):
total=total+i
    print "the total of 1+2+3+4+5...+200 equals", total

n=202
total=1
for i in range (1,n,2):
total=total*i
    print "the total of 1*3*5*7...*201 equals", total

n=6
total=1
for i in range (1,n,2):
total=total*i
    print "the toal of 1*3*5 equals", total

n=11
total=0
for i in range (1,n):
    total=total+i
    print "the sum of 1+2+3+4+5+...10 equals", total