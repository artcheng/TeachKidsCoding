# When you do programing, you should think how to apply your program to more cases
# what if your family has more or less people? What is you have more or less task?

# first, a task should be done only once a day. If you have only 1 or 2 in you task list, you only need 1 or 2 people to do them.
#        So, the inside loop should bask on tasks instead of memebers

# Second, if you want to apply your program to different cases, only 3 things is changeable, memebers, tasks and number of days
#         The rest of program should be never changed again

# Only change these 3 lines if you want to apply your program to other cases
members = ['Mom', 'Dad', 'Hanhan', 'Menmen']
tasks = ['Washes Dish', 'Cleans Floor', 'Cleans Table', 'Others Stuff']
numOfDays = 30

# below should work for all the cases
numOfMember = len(members)
numOfTask = len(tasks)


for day in range (0, numOfDays):
    print 'Day', day+1, ':'

    # When you copy paste a same line of code many times, you should think of loop
    for i in range(0, numOfTask):
        print '\t', members[(day + i) % numOfMember], tasks[i]
    print '\n'  # \n for new line