# Write a function to find the longest common prefix string amongst an array
# of strings.
#
# If there is no common prefix, return an empty string "".


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        strs.sort(key = lambda x:len(x))
        if not strs[0]:
            return ''
        if len(strs) == 1:
            return strs[0]
        for i in range(1,len(strs[0])+1):
            if len(strs[0]) == 0:
                return ''
            s =strs[0][0:i]
            for j in range(1,len(strs)):
                if s!=strs[j][0:i]:return strs[0][0:i-1]
        return strs[0]