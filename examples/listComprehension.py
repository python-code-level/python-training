# list comprehension is created on the fly
# created on the fly during execution
#

# example of list comprehension

location = [x ** 4 for x in range(15)]

print(type(location))
print(len(location))
print(location)

EMPTY="-"
cell = [[EMPTY for i in range(10)] for j in range(5)]

# a 2 d array
print(cell)
print("----------------------------------------------------------------------------------------------")

cell[0][0] = "start"
cell[4][9]= "end"

print(cell)

print("-----------------------------------------------------------------------------------")

threed = [[[EMPTY for i in range(10)] for j in range(5)] for k in range(3)]

print(threed)
print("----------------------------------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------")
threed[0][0][0] = "start"
threed[2][4][9]= "end"

print(threed)

print("-----------------------------------------------------------------------------------")