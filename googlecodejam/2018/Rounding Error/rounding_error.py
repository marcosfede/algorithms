import math

# solution does not pass the last test case...


def solve(npersons, nlanguages, langvalues_original):
    votevalue = 100/npersons
    decimal_votevalue = votevalue - math.floor(votevalue)
    if decimal_votevalue == 0:
        return 100
    accum = 0

    langvalues = [
        x*votevalue for x in (langvalues_original + [0]*(npersons - sum(langvalues_original)))]

    missing_people = []

    langvalues_decimals = list(
        map(lambda lang: lang - math.floor(lang), langvalues))
    for idx, lang in enumerate(langvalues_decimals):
        if lang < 0.5:
            accum += math.floor(langvalues[idx])
            missing_people.append(
                (math.ceil((0.5-lang)/decimal_votevalue), lang))
        else:
            accum += math.ceil(langvalues[idx])
            missing_people.append(
                (math.ceil((1.5-lang)/decimal_votevalue), lang))

    # missing_people += [0.5/decimal_votevalue]*(npersons - sum(langvalues))

    missing_people_ordered = sorted(missing_people, key=lambda x: x[0])

    remaining = npersons - sum(langvalues_original)
    while remaining > 0:
        if remaining >= missing_people_ordered[0][0]:
            remaining -= missing_people_ordered[0][0]
            accum += 1
            nueva_suma = missing_people_ordered[1][0] + \
                missing_people_ordered[0][0]*decimal_votevalue
            nueva_suma = nueva_suma - math.floor(nueva_suma)
            accum += math.floor(missing_people_ordered[0][0]*votevalue)
            if nueva_suma < 0.5:
                nuevaTupla = (math.ceil((0.5-nueva_suma) /
                                        decimal_votevalue), nueva_suma)

            else:
                nuevaTupla = (
                    math.ceil((1.5-lang)/decimal_votevalue), nueva_suma)
            missing_people_ordered.append(nuevaTupla)
            missing_people_ordered.pop(0)

            sorted(missing_people, key=lambda x: x[0])
        else:
            accum += math.floor(remaining*votevalue)
            break

    return accum


def read_input():
    ncases = int(input())
    for case in range(1, ncases + 1):
        n, l = map(int, input().split(" "))
        ci = list(map(int, input().split(" ")))
        sol = solve(n, l, ci)
        print('CASE #{}: {}'.format(case, sol))


read_input()
# print(solve(3, 2, [1, 1]))
