from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
  
        totalOparation = 0
        for i in nums:
            if i < k:
                return -1
        if sum(nums) == k*len(nums):
            return 0
        def downGrade(nums, k):
            nonlocal totalOparation
            nums.sort()
      
            tmp = 0
            secoundBiggestValue = None
            for i in nums:
                if i < k:
                    return -1
                if i > tmp:
                    secoundBiggestValue = tmp
                    tmp = i
            
            for a in range(len(nums)):
                if nums[a] > secoundBiggestValue:
                    nums[a] = secoundBiggestValue
            if secoundBiggestValue != None:
                totalOparation+=1
            if sum(nums) != k*len(nums):
                downGrade(nums, k)

            return totalOparation


        return downGrade(nums, k)

slt = Solution()
print(slt.minOperations([5,2,5,4,5],2))