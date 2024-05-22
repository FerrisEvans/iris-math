import itertools

letters = "ABC"

# find all combinations containing 2 letters

cmb = itertools.combinations(letters, 2)

for val in cmb:
    print(val)

per = itertools.permutations(letters, 2)

for val in per:
    print(val)

per = itertools.permutations(letters)

for val in per:
    print(val)