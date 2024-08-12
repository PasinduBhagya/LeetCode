from typing import List

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        possibleSquareSizes = []
        currentLagest = 0
        counter = 0
        currentLagest = 0
        finalCounter = 0
        for i in range(len(rectangles)):
            val1 = rectangles[i][0]
            val2 = rectangles[i][1]
            
            if val2 >= val1:
                possibleSquareSizes.append(val1)
            else:
                possibleSquareSizes.append(val2)

        sortedUnique = list(set(possibleSquareSizes))
        for sortedUniqueValue in sortedUnique:
            for value in possibleSquareSizes:
                if sortedUniqueValue == value:
                    counter += 1
                       
            if currentLagest < sortedUniqueValue:
                currentLagest = sortedUniqueValue
                finalCounter = counter
            
            counter = 0
        
        
        return finalCounter 
            
solution = Solution()

rectangles = [[8,6],[3,12],[3,9],[8,5],[1,5]]

print(solution.countGoodRectangles(rectangles))