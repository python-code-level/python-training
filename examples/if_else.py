# if else conditionals

high = 10
medium = 5
low = 1

score = 5

if score > low:
    print("high score!")
else:
    print("you won")

# elif is used to check multiple statements
# codes stops and is enacted when a true statement is found


# nesting if else
if test:
    if another_test:
        action()
    else:
        another_action()
else:
    this()

# cascade of if-elif-else
if score > high:
    print("high score!")
elif score > low and score < high:
    print("medium score")
else:
    print("you won")



#
