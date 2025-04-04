class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        firsOccarence = -1
        cI = 0 
        while cI < len(haystack):
            clear = haystack[cI:]
            clear = clear[:len(needle)]
            if needle == clear:
                firsOccarence=cI
                break
            cI+=1
        return firsOccarence
    

slt = Solution()
print(slt.strStr("sadbutsad",'sad'))