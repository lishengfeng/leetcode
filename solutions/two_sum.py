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