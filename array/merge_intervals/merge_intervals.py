from collections import namedtuple

Interval = namedtuple('Interval', ['start', 'end'])


# O(n*logn) for sorting. merging takes linear time


def merge_intervals(arr):
    arr.sort(key=lambda x: x.start)
    new = [arr[0]]
    for i in arr[1:]:
        last = new[-1]
        if i.start > last.end:
            new.append(i)
        else:
            new[-1] = Interval(last.start, max(i.end, last.end))
    return new


if __name__ == "__main__":
    given = [[1, 3], [2, 6], [8, 10], [15, 18]]
    given_intervals = [Interval(*i) for i in given]
    expected = [[1, 6], [8, 10], [15, 18]]
    print("input: ", given)
    print("result: ", [[interv.start, interv.end]
                       for interv in merge_intervals(given_intervals)])
    print("output should be: ", expected)
