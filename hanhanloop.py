n=11
total=0
for i in range (1,n):
    total=total+i
    print "the sum of 1+2+3+4+5+...10 equals", total

#task 3: figure out the total of 1+2+3+4+5.....+200, print "the total of 1+2+3+4+5...+200 equals" xxx
#task 4: figure out the total of 1*3*5*7....*201, print "the total of 1*3*5*7...*201 equals" xxx
r=201
total=0
for f in range(1,r):
    total=total+f
    print "the sum of 1+2+3+4+...200 equals", total
    #task 3: figure out the total of 1+2+3+4+5.....+200, print "the total of 1+2+3+4+5...+200 equals" xxx
#task 4: figure out the total of 1*3*5*7....*201, print "the total of 1*3*5*7...*201 equals" xxx

# figure out the total of all odd number between 1-15
a=16
total=0
for i in range(1,a,2):
    total=total+i
print 'odd numbers=',total

b=202
total=1
for c in range(1,b,2):
    total=total*c
print "1*3*5...201=",total

#task 5:divide 1339928042684663702626654216353741866828222367324552136009000175903930373973956200201339808971908813302485337859343555595880232757068702494068539027184400769291974725364464819431304931640625 by all the even numbers between 2...400.
b=1339928042684663702626654216353741866828222367324552136009000175903930373973956200201339808971908813302485337859343555595880232757068702494068539027184400769291974725364464819431304931640625
a=400
total=1
for a in range(2,a,2):
    total=total*a
print "all even numbers timed=",total
c=b/total
print c

#placeholder
announcement="banana eats %s pounds of catfood in a week"
a=3
b=7
c=3*7
print announcement %c


catfood="the catffod is going to last %s days"
a=6
b=96
c=b/a
print (catfood %c)

Petsitting="Raina makes %s dollars"
a= 60
dogs=2
days= 6
total= a*b*c
print Petsitting %total


n=2791
isPrime = True
for i in range(2, n):
    if n%i == 0:
        isPrime = False
        break         # how to exit a loop in the middle

if isPrime:
    print n, 'is a prime number'
else:
    print n, 'is a composite number'


n=23
The_sisters=True
for i in range(2,n):
    if n%i==0:
        The_sisters=False
        break

if The_sisters:
    print n,'is a prime number'
else:
    print n, 'is a composite nuumber'

#task six
# Brooke and Raina found a pot of 20 gold coins in their backyard.
# They have a replication machine. When they put the gold coins in the replication machine, it reproduces 20 magical coins each week.
# Each week, Banana, the family cat, secretly smuggles out 10 magic coins to get pebbles from scout, their next door neighbor's dog.
# Your task, tell the computer to figure out how many coins do Brooke and Raina have every week of the year.

#task seven
#all other conditions remain the same, except the replication machine got crazy, and it doubles the total number of coins created the previous week.
# tell the computer to figure out the number coins Brooke and Raina have each week now?

found_coins=20
magic_coins=20
banana_steal=10
coins=found_coins

for week in range (1,53):
    coins=coins+magic_coins-banana_steal
    print ("week &s= &s" % (week, coins))


