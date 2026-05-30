class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2

        left, right = 0, m

        while left <= right:
            i = left + (right - left) // 2   # partition in nums1
            j = half - i                      # partition in nums2

            # Edge values - handle boundaries
            maxLeft1  = float('-inf') if i == 0 else nums1[i-1]
            minRight1 = float('inf')  if i == m else nums1[i]
            maxLeft2  = float('-inf') if j == 0 else nums2[j-1]
            minRight2 = float('inf')  if j == n else nums2[j]

            # Valid partition found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Odd total
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                # Even total
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2

            # Too many from nums1 in left half
            elif maxLeft1 > minRight2:
                right = i - 1

            # Too few from nums1 in left half
            else:
                left = i + 1