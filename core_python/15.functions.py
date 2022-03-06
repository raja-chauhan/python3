a= 1
b=10

c = sum((a,b)) # two parenthesis needed
print(c)


# define funciton
def myFunc():
    print('hello')

myFunc()

#  function with parameters

def myFunc2(my_name):
    print('hello ',my_name)
    return ''

myFunc2('rohit')
myFunc2(my_name='raja') 


print(myFunc.__doc__)