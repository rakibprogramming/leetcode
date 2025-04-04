from typing import List 
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        maxValue=-1
        calcls = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    calcls+=1
                    value = (nums[i]-nums[j])*nums[k]
                    if value > maxValue:
                        maxValue = value
        if maxValue <= 0:
            return 0
        else:
            return maxValue

slt = Solution()
