import pprint

thisDict = {
    "key1":1,
    "key20":2,
    "key3":3,
    "key25": 2,
    "key12": 2
}

print(len(thisDict))
print(thisDict)

pprint.pprint(thisDict)

# dictionary values

getValue = thisDict["key20"]
# error if key missing - obs
#getOtherValue = thisDict["key200000"]

print(getValue)

# for search keys - choose list or tuple?
searchKeys = ("key1", "key3", "key5000")
searchKeysAlt = ("key1", "key3", "key5000")

for searchKey in searchKeys:
    if searchKey in thisDict:
        print(searchKey, "gives value: ", thisDict[searchKey])
    else:
        print(searchKey, "not in this dictionary")

print("-------------------------------------")
# dictionaries have a keys method .keys()
print(thisDict.keys())
print("-------------------------------------")
# dictionaries have an items method .items()
print(thisDict.items())
# this returns a list of tuples , each tuple is a key-pairs

print("-------------------------------")

# for (tuple) in {dictionary}
# so the whole tuple can be used like a list or variable to loop

for key, val in thisDict.items():
    print(key, "links to: ", val)

print(" -------------------------------------  ")
for val in thisDict.values():
    print(val)

# generally more useful to find a value from its key, rather than just use values


#' change or update values
thisDict["key20"] = 5000000000000
print(thisDict)

thisDict["newKey"] = 999999
print(thisDict)

thisDict.update({"newKey" : 88888})
print(thisDict)

thisDict.update({"newKeySSS" : 777})
print(thisDict)

# to remove a key-pair, just remove the key
del thisDict["newKey"]
print(thisDict)

print(" XXXXXXXXXXXXXx")

# copy and delete
newDict = thisDict.copy()
del newDict["newKeySSS"]
print(newDict)
print("------------------------------------")

finalDict = {}
finalDict.update(newDict)
finalDict.update(thisDict)
print(finalDict)

print("--------------------------------------------")


checks = (
    ("one",1),
    ("two", 2)
     )

checkDict = {}
checkDict.update(checks)
print(checkDict)

alDict = dict(checks)
print(alDict)





