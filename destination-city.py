from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        destCity = paths[0][1] # B

        for i in range(len(paths)): 
            for j in range(len(paths)):
                if destCity in paths[j][0]:
                    destCity = paths[j][1]
                    break
            

        print(destCity)

solution = Solution()

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

solution.destCity(paths)