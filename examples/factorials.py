# factorials

# 0!  ,   1! etc
# factorial is equal to the product of all natural numbers from one, up to the argument
# reminder, natural numbers = positive integers,

# 2! = 1  * 2
# 3! = 1 * 2 * 3

def factorials(n):
    if n < 0:
        print("must be whole number > 0")
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n+1):
        product *= i
    return product

# tests
for n in range(1,6):
    print(n, factorials(n))


