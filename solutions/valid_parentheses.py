# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input # string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) == 1:
            return False
        parentheses = {')': '(', '}': '{', ']': '['}
        existing_left = []
        latest_parenthese = ''
        for c in s:
            print(c)
            if c in parentheses.values():
                if latest_parenthese:
                    existing_left.append(latest_parenthese)
                latest_parenthese = c
                continue
            if c in parentheses.keys():
                if latest_parenthese != parentheses[c]:
                    return False
                else:
                    latest_parenthese = existing_left.pop() if existing_left\
                        else ''

        if not existing_left and not latest_parenthese:
            return True
        else:
            return False