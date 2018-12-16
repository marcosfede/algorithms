# p1
cl = [3, 7]
elf1 = 0
elf2 = 1
offset = 293801
minscores = offset + 10

while len(cl) < minscores:
    elf1_score = cl[elf1 % len(cl)]
    elf2_score = cl[elf2 % len(cl)]
    newscore = elf1_score + elf2_score
    for digit in str(newscore):
        cl.append(int(digit))

    elf1 = (elf1 + elf1_score + 1) % len(cl)
    elf2 = (elf2 + elf2_score + 1) % len(cl)
print(''.join([str(x) for x in cl[offset:minscores]]))

seek = [2, 9, 3, 8, 0, 1]
for i in range(len(cl)):
    if cl[i:i+6] == seek:
        print('found', i)


cl = [3, 7]
elf1 = 0
elf2 = 1
offset = 21000000
minscores = offset + 10

while len(cl) < minscores:
    elf1_score = cl[elf1 % len(cl)]
    elf2_score = cl[elf2 % len(cl)]
    newscore = elf1_score + elf2_score
    for digit in str(newscore):
        cl.append(int(digit))

    elf1 = (elf1 + elf1_score + 1) % len(cl)
    elf2 = (elf2 + elf2_score + 1) % len(cl)

seek = [2, 9, 3, 8, 0, 1]
for i in range(len(cl)):
    if cl[i:i+6] == seek:
        print('found', i)
