class Solution:
    def find_median_sorted_arrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m > n:
            # Swap array. Make size of nums2 always bigger then nums1
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0:
            return ValueError

        # [1, 2] [3, 4, 5] half_len = 3 j = 3 -1 = 2
        half_len = (m + n + 1) // 2
        # start from the middle
        i = m // 2
        while i <= m:
            j = half_len - i
            if i > 0 and nums1[i-1] > nums2[j]:
                i = i - 1
            elif i < m and nums2[j-1] > nums1[i]:
                i = i + 1
            else:
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums2[j-1], nums1[i-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums2[j], nums1[i])

                return (max_of_left + min_of_right) / 2.0


sol = Solution()
print(sol.find_median_sorted_arrays([1, 2, 3], [4]))
print(sol.find_median_sorted_arrays([1, 2], [3]))
print(sol.find_median_sorted_arrays([1, 3, 5, 7], [2, 4, 6, 8, 10]))
print(sol.find_median_sorted_arrays([1], [2, 4, 6, 8, 10]))
print(sol.find_median_sorted_arrays([1, 5], [2, 4, 6, 8, 10]))




