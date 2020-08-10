from collections import Counter

def find_it(seq):
    counted = Counter(seq)
    for item in counted.items():
        if item[1] % 2 != 0:
            return item[0]


# add k v pairs with number and count of number
# Idenitfy odd count
# Return number
