# For loop is picking up items in a list one by one and doing something

# Some soccer players are exercising. They lined up as a list and practise shooting one by one

team = ['Luck', 'Noah', 'Parker', 'Dayuan', 'Tim']

for player in team:
    # Do something! the lines of code inside loop have same white space in the front.
    print player,' put the ball in front of the goal.'
    print player,' is shooting!'
    print player,' goes to get the ball back.\n'

print '----- take a rest ----'
# Now Jimmy comes, he stands at the end of the line
team.append('Jimmy')
# They practise shooting again

for player in team:
    print player,' is shooting!'

print '----- take a rest ----'
# remember we could use index number to access item in the list
# The coach said, the third player go to collect the balls and the fourth player go to pick up the cones

print team[2], ', Go to collect the balls!'  # We use index 2 to access the third item
print team[3], ', Go to pick up the cones!'  # We use index 3 to access the fourth item

print '----- offense and defense training. every time come out two players, one play offense and one play defense ----'
# this time we use index
n = len(team) # how many players in the team

for i in range(0, n-1):
    print team[i], 'and', team[i+1], 'are practising offense and defense'


print '----- take a rest ----'
for i in range(0, n-1, 2):  # add step 2
    print team[i], 'and', team[i+1], 'are practising offense and defense'

