from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexDict = {}
        ansList = []
        
        for i in range(len(nums)):
            indexDict[i] = nums[i]

        for j in range(len(nums)):
            indexDict[j]
            for k in range(len(nums)):
                if len(ansList) != 0:
                    ansList.sort()
                    return ansList
                if indexDict[j] + indexDict[k] == target and j != k:
                    ansList.append(j)
                    ansList.append(k)
                    break 
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         indexDict = {}
        
#         for i, num in enumerate(nums): # i=0 num=3 # i=1 num=3
#             print(indexDict) # {3: 0}
#             complement = target - num # 6 - 3 = 3 # 6 - 3
#             if complement in indexDict: # 3 {}
#                 return [indexDict[complement], i]
#             indexDict[num] = i # {3: 0}
            
        
#         return []
            
            
          
solution = Solution()

nums = [3,3]
target = 6

print(solution.twoSum(nums, target))
    