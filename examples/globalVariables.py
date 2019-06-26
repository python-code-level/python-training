var = 1
print(var)

def thisFunction():
    var = 5
    print("Accessing var: ", var)

print(var)
thisFunction()
print("---------------------------------------------------------------------------")
def anotherFunction():
    global var
    # no new local varible var is created, just uses the existing global
    var = 5
    print("Accessing var: ", var)

anotherFunction()

print (var)

# global allows the function to modify variables within thw wider body,
# this gives the named variabel global scope