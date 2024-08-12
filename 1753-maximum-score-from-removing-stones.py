import heapq

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        intList = [-a,-b,-c]
        heapq.heapify(intList)
        count = 0
    
        
        while len(intList) > 1:
            first, second = heapq.heappop(intList) + 1, heapq.heappop(intList) + 1
            count +=1
            
            if first < 0: heapq.heappush(intList, first)
            if second < 0: heapq.heappush(intList, second)
        
        return count
        
    
        
                        
solution = Solution()

a = 4
b = 4
c = 6

# solution.maximumScore(a,b,c)
solution.maximumScore(a,b,c)
