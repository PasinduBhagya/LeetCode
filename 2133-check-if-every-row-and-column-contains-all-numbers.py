from typing import List

class Solution:   
    def checkValid(self, matrix: List[List[int]]) -> bool:
        status = "true"
        arrayLength = len(matrix)
        possibleValues = []
        for i in range(arrayLength):
            possibleValues.append(i+1)
        
        for row in matrix:
            if status == "false":
                break
            for possibleValue in possibleValues:
                if possibleValue not in row:
                    status = "false"
                    return status

        for possibleValue in possibleValues:
            if status == "false":
                break
            for l in range(arrayLength):
                columnLists = []
                for m in range(arrayLength):
                    columnLists.append(matrix[m][l])
                if possibleValue not in columnLists:
                    status = "false"
                    return status
        
        return status

solution = Solution()

matrix = [[1,1,1],[1,2,3],[1,2,3]]
print(solution.checkValid(matrix))


                