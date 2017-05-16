import time
import math

# find all the prime number < N
N=50000

start = time.time()
print 'Find all prime number less than', N
for n in range(2, N+1):
    isPrime = True
    for i in range(2, n):  # from 2 to n-1, checking if any number is a factor of n
        if n % i == 0:
            isPrime = False
            break  # how to exit a loop in the middle

    if isPrime:
        print n

end = time.time()
print 'use', end - start, 'seconds'


# but we don't need check factor up to n-1, we could stop at sqrt(n). See how faster it get.
start = time.time()
print 'Find all prime number less than', N
for n in range(2, N+1):
    isPrime = True
    for i in range(2, int(math.sqrt(n))):  # from 2 to n-1, checking if any number is a factor of n
        if n % i == 0:
            isPrime = False
            break  # how to exit a loop in the middle

    if isPrime:
        print n

end = time.time()
print 'use', end - start, 'seconds'

# Another way to find prime numbers, which is used 250BC in Ancient Greece and about 200
start = time.time()
A = range(0, N+1)
n=2
while n<N:
        if A[n] != 0:
                print A[n]
                j = 2*n
                while j<N+1:
                        A[j]=0
                        j=j+n
        n=n+1

end = time.time()
print 'use', end - start, 'seconds'


