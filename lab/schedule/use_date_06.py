from datetime import date
from datetime import timedelta

members = ['Mom', 'Dad', 'Hanhan', 'Menmen']
tasks = ['Washes Dish', 'Cleans Floor', 'Cleans Table', 'Others Stuff']
numOfDays = 30

# below should work for all the cases
numOfMember = len(members)
numOfTask = len(tasks)

date = date.today()
for day in range (0, numOfDays):
    date = date + timedelta(days=1)
    print 'Day', day+1, ':', str(date)

    # Should loop on tasks instead of members
    for i in range(0, numOfTask):
        print '\t', members[(day + i) % numOfMember], tasks[i]
    print '\n'  # \n for new line