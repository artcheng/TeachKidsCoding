# A list is a special data type that holds an ordered collection of items.

lst = [1, 'aha', 3.0, True]

# we use index to access each item, the index of first item is 0
print lst[0]  # first item
print lst[1]  # second item
print lst[2]
print lst[3] # last item


# Most of the time, all the items are same type. Some language even requires all the items in the list are same type
list =  [1, 5, 8, 16]
print list

list = ['Metal', 'Wood', 'Water', 'Fire', 'Earth']
print list

# You can create a list of numbers using range function. What is function? we will talk about it later. For now, just use it.
list = range(0, 10)  #a list of integer form 0 to 9
print list

list = range(0, 10, 2)  # if you want to count by 2
print list

# Most of data type has build-in method.  Look how to append one more item to a list
list = [] # empty list
print list
list.append("one")
print list
list.append("two")
print list

