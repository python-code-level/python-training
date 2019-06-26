# simple example calc function
# multiple returns can be used inside a function

def bmicalc(weightKg, heightM):
    # set protection checks for extreme values
    if heightM < 1 or heightM > 2.5 or \
    weightKg < 20 or weightKg > 200:
        print("check data entry")
        return None
    # for valid values return weight / height raised to the power 2
    return weightKg / heightM ** 2


print(bmicalc(0.5,100))
print(bmicalc(75, 1.7))


# helper functions
# a block of code that get used several or many times, and canhelp with other \
# more complex functions, is a helper function
# conversions, averages, etc, etc,
# it performs part fo the calculatino occuring within another function,
# helper functinos begin to extend the idea of having functions within functions


