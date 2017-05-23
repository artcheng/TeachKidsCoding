# look at basic_01.py.  if you want to print a schedule of 30 days, you should think of dor a for loop on days

members = ['Mom', 'Dad', 'Hanhan', 'Menmen']
tasks = ['Washes Dish', 'Cleans Floor', 'Cleans Table', 'Others Stuff']

for day in range (0, 30):
    print 'Day', day+1, ':'
    print '\t', members[0], tasks[0]  # \t for tab
    print '\t', members[1], tasks[1]
    print '\t', members[2], tasks[2]
    print '\t', members[3], tasks[3]
    print '\n'  # \n for new line

# however, the job is fixed to each person! How to deal with that.
# Observe teh basic_01.py. the order of tasks should be
# 0,1,2,3
# 1,2,3,0
# 2,3,0,1
# 3,0,1,2
# 0,1,2,3
# 1,2,3,0
# 2,3,0,1
# 3,0,1,2
# ......

# how to generate a pattern like this?