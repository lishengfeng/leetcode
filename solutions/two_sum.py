# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you
# may not use the same element twice.


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        possible_values = {}
        for index, val in enumerate(nums):
            if val in possible_values:
                return [possible_values[val], index]
            else:
                possible_values[target-val] = index