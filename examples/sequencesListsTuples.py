lits1 = [1,2,3,4,5]
tuple1 = (10,20,30,40)
lits1.append(500)

# no append method for tuples
#tuple1.append

print(lits1)
print(tuple1)
print(type(tuple1))
print(type(lits1))


a = 1
b = 1,
c = (1)

print(a, b, c, sep="        ")


print("------------------------------------")

shortTuple = 1, 4, "ten", "eleven"
longTuple = (1,2,3,55,66,7,8,9,9,9,9,9,9,9,9,)

# not possible for tuples
# del longTuple[:5]

print(len(longTuple))

thisTuple = shortTuple+longTuple

print(thisTuple)

