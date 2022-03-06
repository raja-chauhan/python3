def function1(a,b,c,d):
    print(a,b,c,d)

function1(1,2,3,4)

"""
but if have no fixed length of argumets passes to function in that case what will i do


"""
def function2(*args):
    print(args[:])
    print(type(args))


function2(1,2,3,4,5,65,76,76,45)
function2(1,2,4)


# kwargs -> key and value pair passes dictionary
def function3(normal_argument,*args,**kwargs):
    print(normal_argument)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,value)


function3('normal argument',[1,2,3,4,5],{'name':'raja','age':24})