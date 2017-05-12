#For loop
for student in ["Tom", "Lucy", "Jack", "Chris"]:
    print "How are you!", student, "!"

for i in range(0, 10):
    print i

print '-'*10

#what is range(0, 10)
print range(0, 10)

print '-'*10
a=10
for i in range(0, a):
    print i,"'s square is ", i*i

print '-'*10

#if you want to stop a loop in the middle, use break
a=100
for i in range(0,a):
    print i
    if i>10:
        break

print '-' * 10

# understand the space in front each line.
#1.
a=5
for i in range(0, 5):
    x=i**2 #Do something inside the loop
    print 'inside the for loop, i is ',i  #i is changing every time

print '-' * 10
#2
for i in range(0, 5):
    x=i**2 #Do something inside the loop
print 'outside the for loop, i is ',i  #i is the last value when get out the loop



print '-' * 10
#example 1. calculate 1+2+3+...+100
n=101
sum=0

for i in range(1, n):
    sum = sum + i
print sum

#task 1. calculate 15!=1*2*3*...*15


print '-' * 10
#example 2. Find all factor of a given number
n=4983

print 'finding', n, '\'s factors'  #if you want to print ', use \', just like \n for a new line
for i in range(2, n):
    if n%i==0:
        print i, 'is a factor of', n
print 'finding factors of ', n

