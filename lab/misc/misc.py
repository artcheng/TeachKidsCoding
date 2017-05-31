import time
start = time.time()
n=100000000
total=0
for i in range (1,n+1):
    total=total+i

end = time.time()
print "the total of 1+2+3+4+5...+",n,"equals", total, 'loop uses', end - start, 'seconds'

print "---------"
start = time.time()
total = n*(n+1)/2

end = time.time()
print "the total of 1+2+3+4+5...+",n,"equals", total, 'formula use', end - start, 'seconds'

