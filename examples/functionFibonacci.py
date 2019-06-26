def fibonacci(n):
    # catch examples where n < 1
    if n < 1:
        return None
        # same as
        # return
    # catch examples where n < 3
    if n < 3:
        return 1
    # for values = or > 3
    # set first and second elements to 1
    elem1 = elem2 = 1
    sum = 0
    # loop over numbers for 3 to
    for i in range(3, n + 1):
        sum = elem1 + elem2
        elem1, elem2 = elem2, sum
    return sum



# test the function

print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(8))