# functions can return with or without an expression
# when return is reached, it exits the function

def example(full = True):
    print("start")
    if full:
        return
    print("stop")

# check

example()
print("---")
example(full=False)

print(" ---------------------------------------------------- ")

#

def functionNone(number):
    # if odd
    if (number % 2 ==0):
        return True


print(functionNone(1))
print(functionNone(2))
print(functionNone(3))
