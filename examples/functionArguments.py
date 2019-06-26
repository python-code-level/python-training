
def aFunction(num):
    num += 1
    print("how many:", num)

var = 1
print(var)
aFunction(1)
print(var)

# the above functions has no impact on the number var within main body
# this is also the same behaviour if the variables and paramter have same name

# the function receives the arguments value, not the argument itself (for scalars)

print("-----------------------------------   1    --------------------------------------------")
# a list example

def listFunction(aList):
    print(aList)
    # select data from the list
    aList = [0,10,20]
    # function has effect, but returns None

bList = [0,100,200]
listFunction(bList)
print(bList)

print("------------------------------------   2    -------------------------------------------")
# a list example
# trying to modify the entire list, does not change the arguments contents

def listFunction(aList):
    print(aList)
    # select data from the list
    aList = [0,10,20]
    return aList
    # function has effect, returns list

bList = [0,100,200]
listFunction(bList)
print(bList)

print("------------------------------------   3    -------------------------------------------")
# a list example

print("------------------------------------   4    -------------------------------------------")
# a list modification example
# changing the values within the supplied argument, does propogate outside the function

def listFunction(aList):
    print(aList)
    # select data from the list
    del aList [0]
    # function has effect

bList = [0,100,200]
listFunction(bList)
print(bList)

print("------------------------------------   5    -------------------------------------------")

def listFunction(aList):
    print(aList)
    # select data from the list
    aList.append(555)
    # function has effect

bList = [0,100,200]
listFunction(bList)
print(bList)

print("------------------------------------   6    -------------------------------------------")

# lists cannot be reasigned but can be sorted, appended, delete VALUES inside the list

def listFunction(aList):
    print(aList)
    # select data from the list
    aList.sort()
    # function has effect, but returns None

bList = [8000, 50, 0,100,200]
listFunction(bList)
print(bList)

print("------------------------------------   6    -------------------------------------------")








