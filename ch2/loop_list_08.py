# while loop

n=10

while n>0:  # n>0 is the condition, as long as the condition is True, the loop will go on.
    print 'I have', n, 'apples, I will eat one'
    n = n - 1

print 'I have no apple left'

# more on list

lst = ['Apple', 'Grape', 'Orange', 'Pineapple']

# task 1: print I like Orange
print 'I like', lst[2]

# task 2: Use Watermelon to replace pineapple
lst[3] = 'Watermelon'  # how to change a value in the list
print lst


# task 3
nums = range(1, 10)
print nums

# 3.1 Change all the even number to 0
i = 1

while i < len(nums):
    nums[i] = 0
    i = i+2

print nums

# you need make sure while loop could stop at certain condition, otherwise, it is a dead loop

i = 0
while i<5:
    print i
    i = i+1  # without this line, it will be a dead loop and print 0 forever


i = 0
while True:   #We design the loop to loop "forever" on purpose
    print i
    i = i+3

    # but we could stop it at certain point
    if i%5 ==0:
        break



