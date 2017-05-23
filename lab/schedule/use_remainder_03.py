members = ['Mom', 'Dad', 'Hanhan', 'Menmen']
tasks = ['Washes Dish', 'Cleans Floor', 'Cleans Table', 'Others Stuff']

for day in range (0, 30):
    print 'Day', day+1, ':'
    print '\t', members[0], tasks[day%4]  # variable day keeps increasing, once you %4, it points to different start point every time
    print '\t', members[1], tasks[(day+1)%4]
    print '\t', members[2], tasks[(day+2)%4]
    print '\t', members[3], tasks[(day+3)%4]
    print '\n'  # \n for new line