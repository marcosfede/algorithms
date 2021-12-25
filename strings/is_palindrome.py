"""
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem,
we define empty string as valid palindrome.
"""


def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

# Time Complexity : O(len(s))
# Space Complexity : O(1)


def is_palindrome_pythonic(s):
    """
    :type s: str
    :rtype: bool
    """
    alphanumerics = [c.lower() for c in s if c.isalnum()]
    return alphanumerics == alphanumerics[::-1]

# Time Complexity : O(len(s))
# Space Complexity : O(len(s))
