import cProfile
cp = cProfile.Profile()
cp.enable()

list=[1,2,3,4667,889,553,]
list.reverse()
print(list)

# Sorting a large, randomly generated string and writing it to disk
import random

#def write_sorted_letters(nb_letters=10**7):
def write_sorted_letters(nb_letters=4 ** 5):
    random_string = ''
    for i in range(nb_letters):
        random_string += random.choice('abcdefghijklmnopqrstuvwxyz')
    sorted_string = sorted(random_string)

    with open("sorted_text.txt", "w") as sorted_text:
        for character in sorted_string:
            sorted_text.write(character)

write_sorted_letters()



cp.disable()
cp.print_stats()