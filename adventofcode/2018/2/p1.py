from collections import Counter

with open('./input') as f:
    lines = f.readlines()
    twos = 0
    threes = 0
    for line in lines:
        c = Counter(line)
        values = c.values()
        if 2 in values:
            twos +=1
        if 3 in values:
            threes +=1

    print(twos)
    print(threes)
    print(twos*threes)
