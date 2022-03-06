# it can hold both string and number at the same time

grocery = ['apple',10,'mango',20,'orange',30,'grapes',40]

print(grocery)

# indexing similar to string
print(grocery[0])
print(grocery[:])
print(grocery[:5])
print(grocery[5:])
print(grocery[::-1])

# ================================== list function ==================================

# find the length of list,max and min
# len(list_name)
# max(list_name)
# min(list_name)

grocery.append('new_value')
# at specefic index
grocery.insert(1,'another_value')
# remove item
grocery.remove('apple')
# remove last elements
grocery.pop()
print(grocery)

