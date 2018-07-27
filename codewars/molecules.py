from collections import Counter


def parse_molecule(formula):
    stack = [[]]
    left = {'(', '[', '{'}
    right = {')', ']', '}'}
    numb = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    i = 0
    l = len(formula)
    while i < l:
        c = formula[i]
        if c in left:
            stack.append([])
        elif c in right:
            ind = i
            while ind + 1 < l and formula[ind + 1] in numb:
                ind += 1
            stack[-1] = stack[-1] * int(formula[i + 1:ind + 1] or 1)
            tmp = stack.pop()
            stack[-1] += tmp
            i += ind - i
        elif c in numb:
            ind = i
            while ind + 1 < l and formula[ind + 1] in numb:
                ind += 1
            stack[-1] = stack[-1][:-1] + [stack[-1][-1]] * int(formula[i:ind + 1])
            i += ind - i
        elif c.lower() == c:
            stack[-1][-1] += c
        else:
            stack[-1] += c
        i += 1
    return dict(Counter(stack[0]))


# print(parse_molecule("K4[ON(SO3)2]2"))
# print(parse_molecule("Mg(OH)2"))
# print(parse_molecule("Mg12"))
print(parse_molecule("(C5H5)Fe(CO)2CH3"))
