members = ['Mom', 'Dad', 'Hanhan', 'Menmen']
tasks = ['Washes Dish', 'Cleans Floor', 'Cleans Table', 'Others Stuff']

for day in range (0, 30):
    print 'Day', day+1, ':'

    # When you copy paste a same line of code many times, you should think of loop
    for i in range(0, 4):
        print '\t', members[i], tasks[(day + i) % 4]
    print '\n'  # \n for new line