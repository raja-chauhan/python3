"""
global variable --> use by all other codes. 
local variable --> declare inside block of code , code is not used by other blocks
"""

# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)


# erro while upate value
# This function uses global variable s
def f():
	s += 'GFG'
	print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
f()


# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s)

# Global Scope
s = "Python is great!"
f()
print(s)
