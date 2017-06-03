#task six
# Brooke and Raina found a pot of 20 gold coins in their backyard.
# They have a replication machine. When they put the gold coins in the replication machine, it reproduces 20 magical coins each week.
# Each week, Banana, the family cat, secretly smuggles out 10 magic coins to get pebbles from scout, their next door neighbor's dog.
# Your task, tell the computer to figure out how many coins do Brooke and Raina have every week of the year.

#task seven
#all other conditions remain the same, except the replication machine got crazy, and it doubles the total number of coins created the previous week.
# tell the computer to figure out the number coins Brooke and Raina have each week now?

a=20
Banana=10
replication=20
coins=20
for week in range(1,53):
    coins=coins*2-Banana
    print "week %s=%s" %(week,coins)

#task seven
#Raina is saving five bucks each week.
#By putting it in the bank, she earns one dollar interests for every five dollars she has each week.
# Please tell the computer how much money does Raina have each week.


