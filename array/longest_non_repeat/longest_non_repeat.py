from typing import Dict


def longest_non_repeat(s: str) -> int:
    start, maxlen = 0, 0
    used_char = {}  # type: Dict[str, int]
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i - start + 1)
        used_char[char] = i
    return maxlen


a = "abcabcdefbb"
print("input: ", a)
print("result: ", longest_non_repeat(a))
print("output should be 6")
