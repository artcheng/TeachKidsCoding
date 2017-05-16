# Let's do some math using for loop
# example 1. calculate 1+2+3+...+100
n = 101
total = 0

for i in range(1, n):  # i from 1 to 100
    total = total+i

print "1+2+3+...+100 =", total  # once the loop finished, the code goes to previous level.


# task 1. calculate 10*9*8*...*1



# example 2. Find all factors of a given number. How to make different levels of code.

n = 2850
for i in range(2, n):
    if n%i == 0:    # for loop
        print i, 'is a factor of', n  # if

# task 2. For a given number, let the computer decide if it is a prime number.



# answer
# let the computer decide if it is a prime number. Understand the how code block
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

