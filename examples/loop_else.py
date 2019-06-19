
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")


for i in range(1, 4):
    if i == 2:
        continue
    print(i)

else:  # Executed because no break in for
    print("No Break")


for i in range(1, 4):
    print(i)
    break
else: # Not executed as there is a break
    print("Break")


# else can be used to determine why / how the loop was left
#
# in these uses, the else can be thought of as "no break"

mylist = ("one", "two" ,"three")
mylist = ("one", "two", "theflag", "four")
for i in mylist:
    if i == "theflag":
        break
    #process(i)
    print(i)
else: # no break found
    raise ValueError("List argument missing terminal flag.")


for x in data:
    if meets_condition(x):
        break
else: # no break
    # raise error or do additional processing


# so, benefit of using else means dont have to create a flag
#

