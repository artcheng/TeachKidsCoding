# build-in Function

print ('Hello world!')  # print function

s = 'Hello world!'
print (s)   # print function take a parameter, and print it on the screen.

print (len(s)) # len function give the length of a list, you see string is actually a list of characters

# functionName( parameters )...function doing something, and / or return a value.

# you can define your own function.
def func( someOne ):
    print 'Hi, ', someOne;

# how to call a function
func('Hanhan')


# define a function with return value
def facorial( n ):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

# call the function to calculate and get the result
m = facorial( 5 )

print '5! = ',m

