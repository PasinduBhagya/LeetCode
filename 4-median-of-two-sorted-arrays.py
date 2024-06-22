from typing import List
from statistics import median

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return median(sorted(nums1 + nums2))
            
        # return mergedList
        
solution = Solution()

nums1 = [1,3]
nums2 = [2]

print(solution.findMedianSortedArrays(nums1, nums2))