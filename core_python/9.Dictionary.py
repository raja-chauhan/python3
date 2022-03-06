# it's a key value pair and always case sensitive

d1 = {}

d2 = {
    1:'raja',
    2:'rohit',
    3:'laloo'
}

print(d1)
print(d2)
print(d2[3])

#  add new key value pair

d2['4'] = 'devank'

# delete property
del d2[1]

# create copy

d3 = d2.copy()

# if you use d3 =d2 then if you change d2 later d3 also change

# update poperty
d2.update({2:'rajesh'})

# to get all keys
d2.keys()

# to get all items
d2.items()


print(d2)