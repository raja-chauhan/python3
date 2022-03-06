mystr = "hello my name is raja chauhan"

print(mystr)
print("mystr[0:5] ",mystr[0:5])
print("mystr[0:] ", mystr[0:])
print("mystr[:5] ",mystr[:5])
print('length of string', len(mystr))

# outof index error
# print("mystr[78]", mystr[78])
# solve it by
print("mystr[0:78]", mystr[0:78])


# skip few indexed
print("mystr[::2]",mystr[::2]) #
# print in reverse
print("reverse print",mystr[::-1])

# ============================================== functions of string ========================

# is alphanumeric check (if it contain space then return false)
"""

    Python String isalpha()
    Python String isdigit()
    Python String isspace()
    Python String isdecimal()
    Python String isprintable()
    Python String isnumeric()
"""

print("isalnum()",mystr.isalnum())


# ends with

print("mystr.endswith('chauhan')",mystr.endswith('chauhan'))

# count character

print("mystr.count('b')",mystr.count('a'))

# capitalize first letter

print("mystr.capitalize()",mystr.capitalize())

# find index of search item

print("mystr.find('is')",mystr.find('is'))

# lower all characters

print("mystr.lower()",mystr.lower())

# upper all characters

print("mystr.upper()",mystr.upper())

# replace method but don't change original value

print("mystr.replace('is','are')",mystr.replace('is','are'))
print(mystr)
