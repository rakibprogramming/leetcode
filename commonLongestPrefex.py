from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = "" #longest prefix that will be return 
        currentCheckingPrefix ="" #current prefix that are being checked
        for i in strs[0]: #Using the first element to check all the elements. Since we need to find the common prefix, we can just use the first element. Using the shortest element would be better, but the array is not sorted.
            currentCheckingPrefix=currentCheckingPrefix+i #updating current checking prefix

            #Set commonPrefix to true and iterate through all the elements. If any element doesn't match the currentCheckingPrefix, there's no need to check the others
            commonPrefix = True 
            for e in strs:
                # e[:len(currentCheckingPrefix)] return the same first numbers of element as currentCheckingPrefix
                if not currentCheckingPrefix == e[:len(currentCheckingPrefix)]:
                    commonPrefix = False
                    break #breaking this loop if the prefix is no common
            if commonPrefix:
                longestPrefix=currentCheckingPrefix #updating the return value if the prefix is common.
            else:
               break #breaking the whole loop. If one element didn't match there is no need for checking others

        return longestPrefix # finnaly, you know what
    

slt = Solution()
print(slt.longestCommonPrefix(["flower","flow","flight"]))