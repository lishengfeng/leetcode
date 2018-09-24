# Given a string s, find the longest palindromic substring in s. You may
# assume that the maximum length of s is 1000.
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"
# Link: https://www.youtube.com/watch?v=nbTSfrEfo6M
# Python to implement Manacher's Algorithms


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$". ^
        # and $ signs are sentinels appended to each end to avoid bounds
        # checking
        if len(s) == 0:
            return ""
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R-i, P[2 * C - i])
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i-1-P[i]]:
                P[i] += 1
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]


sol = Solution()

text1 = "babcbabcbaccba"
print(sol.longestPalindrome(text1))

text2 = "abaaba"
print(sol.longestPalindrome(text2))

text3 = "abababa"
print(sol.longestPalindrome(text3))

text4 = "abcbabcbabcba"
print(sol.longestPalindrome(text4))

text5 = "forgeeksskeegfor"
print(sol.longestPalindrome(text5))

text6 = "caba"
print(sol.longestPalindrome(text6))

text7 = "abacdfgdcaba"
print(sol.longestPalindrome(text7))

text8 = "abacdfgdcabba"
print(sol.longestPalindrome(text8))

text9 = "abacdedcaba"
print(sol.longestPalindrome(text9))
