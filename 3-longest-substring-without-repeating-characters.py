class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringList = list(s)
        maxLen = 0
        
        for i, sinLetter in enumerate(stringList):
            newString = ""
            for uLetter in stringList[i:]:
                if uLetter in list(newString):
                    break
                else:
                    newString += uLetter
                    if len(list(newString)) == len(list(set(list(newString)))):
                        if len(list(newString)) > maxLen:
                            maxLen = len(list(newString))
        
        return maxLen
                   
solution = Solution()
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmn"
print(solution.lengthOfLongestSubstring(s))