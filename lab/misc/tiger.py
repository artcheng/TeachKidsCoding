#create a list named (RPS) that include worm, chicken, wolf, tiger, stick
# create a loop function that prints Chicken beats worm; wolf beats chiceken, tiger beats wolf, stick beats tiger, worm beats stick
RPS=['worm', 'chicken', 'wolf', 'tiger', 'stick']
n=len(RPS)
for p in range (0, n):
    print RPS [(p+1)%n], "beats", RPS [p%n]