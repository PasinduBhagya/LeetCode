class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        splitS1 = list(s1)
        splitS2 = list(s2)
                
        if s1 == s2:
            return True
        
        possibleValue = []
        for i in range(len(splitS2)-1):
            swap1 = splitS2[i]
            for j in range(len(splitS2)-i):
                swap2 = (splitS2[i+j]) 
        
                splitS2[i] = swap2
                splitS2[i+j] = swap1
                
                possibleValue.append(splitS2)
                splitS2 = list(s2)
        if splitS1 in possibleValue:
            return True
        else:
            return False

solution = Solution()

s1 = "bank"
s2 = "kanbw"

print(solution.areAlmostEqual(s1, s2))