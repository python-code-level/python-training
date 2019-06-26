# arguments outside
# parameters inside
#

def function(parameter):
    # command
    print("done")

function(1)

def anotherfunction(parameter):
    parameter+1
    # command
    print("done")

anotherfunction(3)  # the argument 3 is supplied
#anotherfunction("word") # the argument word is supplied

result = 200
print(result)


def doubleInteger(numberParameter):
    result = numberParameter*2
    print(result)
    return result

#doubleInteger(2)
print(doubleInteger(2))

result = 100

print(result)

# shadowing and identity
# although with the same name "result" they are different objects
# inside vs outside the function
# inside the function results "shaows" any other variable outside,
# it is used in preference / higher priority

def announcements(firstName, surName, country):
    if country == "UK":
        print("Announcing: ", firstName, surName)
    elif country == "Italy":
        print("Announcing :", surName, firstName)
    else:
        print("unknown country")

announcements("John", "Smith", "UK")
announcements("Sylvia", "Alba", "Italy")
announcements("Steve", "Wright", "Scotland")

announcements(surName="Smith", country="UK", firstName="richard")

# positional argument must be before keyword arguments

announcements("jim", country="UK", surName="Jones")

# note, it is possible to set defaults when using functions
# so not all arguments need to be passed to the function
# so in the case where ther eis no argument outside,
# a default parameter value already exists inside
#

def announcementsUK(firstName, surName, country="UK"):
    if country == "UK":
        print("Announcing: ", country, firstName, surName)
    elif country == "Italy":
        print("Announcing :", country, surName, firstName)
    else:
        print("unknown country", country)

announcementsUK("John", "Smith")
announcementsUK("Stu", "White")
announcementsUK("Sylvia", "Alba", "Italy")
announcementsUK("Steve", "Wright", "Scotland")

# passing an unknown number of arguments from outside into the function
# at invociation the names object is different each time new arguments are supplied
def introduce(*names):
   # names is a tuple with arguments
   print("names list id:", id(names))
   for name in names:
       print(id(name))
       print("Hello",name)
print("---------------------<<<   >>>--------------------------------")
introduce("steve","john","james")
introduce("philippa")
introduce("doris, daphne")
print("-------------------------------------------------------------")
print("-------------------------------------------------------------")


# using an empty but mutable variable needs caution
# at invocation the empty names list object is the same each new arguments are supplied
# the new list in the parameters overights / replaces the default  list

def introduce(names=[]):
   # names is a tuple with arguments
   print("names list id:", id(names))
   for name in names:
       print(id(name))
       print("Hello",name)

introduce(["steve","john","james"])
print("-------------------------------------------------------------")
introduce(["philippa"])
print("-------------------------------------------------------------")
introduce([])
print("-------------------------------------------------------------")
introduce()
print("-------------------------------------------------------------")

# a function is defined the first time it gets called, then subsequent calls use that

# using an empty but mutable variable needs caution
# example appending to a list
def introduce(names=[]):
   # names is a tuple with arguments
   print("names list id:", id(names))
   names.append("jonty")
   print("names list id:", id(names))
   print(names)
   for name in names:
       print(id(name))
       print("Hello",name)

introduce()
print("+++++++++++++")
introduce()
print("+++++++++++++")
introduce()

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
# this is the recommend pattern to avoid bugs from mutable default params

# using an empty but mutable variable needs caution
# example appending to a list
def introduce(names=None):
    if names is None:
        names = []
    print("names list id:", id(names))
    names.append("jonty")
    print("names list id:", id(names))
    print(names)
    for name in names:
        print(id(name))
        print("Hello",name)

introduce()
print("+++++++++++++")
introduce()
print("+++++++++++++")
introduce()

