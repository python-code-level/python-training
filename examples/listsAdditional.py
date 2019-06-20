alist=[1,2,45,67,987, 888,999]
blist=alist[:] # slice
clist=alist[0:3] # slice
dlist=alist[2:-2]

print(alist)
print(blist)
print(clist)
print(dlist)

del blist[:3]
print(blist)

# empty the list
del blist[:]
print(blist)

del blist
# print(blist)  #cant print, as has been deleted

newlist=[1,2,3,4,56,7,8,99]
print(43 in newlist)  # = False
print(43 not in newlist)  # = True

