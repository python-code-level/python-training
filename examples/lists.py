# lists
listnumbers = [1,2,4,8,16]
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
listnumbers[0] = listnumbers[4]
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("list type:",type(listnumbers))
print(listnumbers[1])
print("---------------------------------------------------------------------")
del listnumbers[0]
print("delete an element, by ref to index")
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("list type:",type(listnumbers))
print("---------------------------------------------------------------------")
del listnumbers[0]
print("delete an element, by ref to index")
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("list type:",type(listnumbers))
# index out of range print(listnumbers[6])
print("---------------------------------------------------------------------")
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("negative index:",listnumbers[-1])
# various methods can be used to modify lists
# methods act on the type list
print("---------------------------------------------------------------------")
listnumbers.append(67) # takes one argument at a time
listnumbers.append(1289) # takes one argument at a time
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("---------------------------------------------------------------------")
listnumbers.append(67) # takes one argument at a time
listnumbers.append(1289) # takes one argument at a time
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("---------------------------------------------------------------------")
listnumbers.insert(0,67) # takes one argument at a time
listnumbers.insert(1,299) # takes one argument at a time
print("list contains:",listnumbers)
print("list elements:",len(listnumbers))
print("---------------------------------------------------------------------")
thelist = []
for i in range(10):
   thelist.append(i+1)
print(thelist)
print("---------------------------------------------------------------------")
thelist = []
for i in range(10):
   thelist.insert(0,i+1)
print(thelist)
print("---------------------------------------------------------------------")
thelist = [12,11,13,14,15]
total=0
for i in range(len(thelist)):
   total +=thelist[i]
print(total)
print("---------------------------------------------------------------------")
thelist = [12,99,11,13,14,15]
total=0
for i in thelist:
   total +=i
print(total)
print("---------------------------------------------------------------------")
print("unsorted list", thelist)
thelist.sort()
print("sorted list", thelist)
thelist.reverse()
print("reversed list", thelist)
print("---------------------------------------------------------------------")
alist=[100]
blist = alist
alist[0]=999
print("alist:",alist)
print("blist:",blist)



