p=9
t=12
if p>t/2:
    print ('you can')
else:
    print ('you cant')

r=6
if r>8:
    print ('pierce')
else:
    print ('no')


#multiply two integers between 1-100. If the result is an even number, print "heavenly bliss," if the result is an odd numeber, print "odd couple"
Hi=4
By=45
if Hi*By%2>0:
    print ('odd couple')
else:
    print ('heavenly bliss')

Place_of_horror=['snake gut','horse poop', 'frog saliva', 'cow puke', 'bat bloood', 'chicken beak', 'cameleon eyeball', 'human tongue', 'shark teeth', 'bird skeleton', 'dog fart']
print (Place_of_horror[7])
print (Place_of_horror[6:9])

Pizza=['peperoni', 'cheese', 'tomato sauce', 'olive', 'flour', ' meat sauce', 'mushroom', 'spinach']
# use len() to count how many items in the list
n = len(Pizza)
print 'there are', n, 'items in the list now'


# List_task_1 print a list of all numbers from 22 to 45
# Task_2 print a list (name it Hit) of all odd numbers between 23-45
# task 3: print a item 4-7 from list Hit
# task 4: add three items to list Hit, "Bulbasuar" "Brooke" and "multiplication"
# task 5: print "there are X numbers of item in list Hit" use len(n) function
list=range(22,45)
print (list)

yellow_car=range(1,100)
print (yellow_car)

Hit=range(23,45,2)
print (Hit)

awesome=range(22,66,2)
print (awesome)
print (Hit[3:7])
print (awesome[4:9])
Hit.append('Bulbasuar')
print (Hit)
Hit.append('Brooke')
Hit.append('multiplacation')
Hit.append ('division')
print (Hit)

n=len(Hit)
print 'there are', n,'numbers' ' in the list'



list=('dough', 'pepperoni', 'pepper', 'cheese', 'tomato paste', 'pineapple cubes', 'ham')
print list
for ingredients in list:
    print (ingredients)
m=len (list)
print "there are", m, "ingredients in the list "
for ingredients in list:
    print "add", ingredients, "into shopping list"

    #task
#Loop exercise
# Make a list including six items that banana likes, call this list BTF
# create a loop function that complete a set of sentences that all begin with "Banana loves ____"

BTF=['pencils','rubber bands','shawls','carpet','watching birds','frog']
print (BTF)
for toys in BTF:
    print 'Bannana loves his', toys

Rlove=['sciense','puff','activtities','toys']
print (Rlove)
for things in Rlove:
    print 'raina loves', things


family=['Tianfu','Sonja','Brooke','Raina','Bannana']
print family[2]
for people in family:
    print people,'needs to speak chinese'

