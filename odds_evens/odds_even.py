def find_outlier(integers):
    odds = []
    evens = []
    for i in integers:
        [evens.append(i) if i % 2 == 0 else odds.append(i)] 
    
    if len(evens) > len(odds):
        return odds[0]
    else:
        return evens[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
#Should return: 11 (the only odd number)

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
