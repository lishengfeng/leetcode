class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        non_rep_list = list()
        longest = 0
        for c in s:
            if c in non_rep_list:
                cur_size = len(non_rep_list)
                if cur_size > longest:
                    longest = cur_size
                d_index = non_rep_list.index(c)
                non_rep_list = non_rep_list[d_index + 1:]
                non_rep_list.append(c)
            else:
                non_rep_list.append(c)
        cur_size = len(non_rep_list)
        return longest if longest > cur_size else cur_size


sol = Solution()
print(sol.lengthOfLongestSubstring('dvdf'))
print(sol.lengthOfLongestSubstring('aab'))
print(sol.lengthOfLongestSubstring(' '))
print(sol.lengthOfLongestSubstring('abcabcabc'))
print(sol.lengthOfLongestSubstring('bbbbbbb'))
print(sol.lengthOfLongestSubstring('pwwkew'))
