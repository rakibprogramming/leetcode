

class Solution:
    def reverseDegree(self, s: str) -> int:
        letters="abcdefghijklmnopqrstuvwxyz"
        revDegree = 0
        for i in range(len(s)):
            revDegree += (26 - letters.index(s[i]))*(i+1)
        return revDegree
    


slt = Solution()

print(slt.reverseDegree("zaza"))