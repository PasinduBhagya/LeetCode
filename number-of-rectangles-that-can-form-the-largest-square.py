from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        possibleSquareSizes = []
        for i in range(len(rectangles)):
            val1 = rectangles[i][0]
            val2 = rectangles[i][1]
            
            if val2 >= val1:
                possibleSquareSizes.append(val1)
            else:
                possibleSquareSizes.append(val2)
                
        finalCounter = 0
        new_counter = 0
        currentLagest = 0
        
        print(possibleSquareSizes)
        
        for j in range(len(possibleSquareSizes)): # [2, 3, 3, 3]
            for k in range(len(possibleSquareSizes)):
                
                if possibleSquareSizes[j] == possibleSquareSizes[k]:
                    new_counter += 1
                    
            if currentLagest < possibleSquareSizes[j]:
                finalCounter = new_counter
                currentLagest = possibleSquareSizes[j]
            new_counter = 0
            
        
        return finalCounter 
              
        
            
solution = Solution()

rectangles = [[3,12],[3,9],[8,5]]

print(solution.countGoodRectangles(rectangles))