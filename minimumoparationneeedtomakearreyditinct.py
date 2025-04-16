from collections import deque
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nums = deque(nums)
        howmanyTime = {}
        for i in nums:
            if i in howmanyTime:
                howmanyTime[i] = howmanyTime[i] + 1
            else:
                howmanyTime[i] = 1
        print(howmanyTime)

        totalOparation = 0

        def removing():
            nonlocal  totalOparation
            for c in howmanyTime:
                howmany = howmanyTime[c]
                if howmany > 1:
                    totalOparation+=1
                    removed = 0
                    while removed < 3:
                        if len(nums) > 0:
                            howmanyTime[nums[0]] = howmanyTime[nums[0]]-1
                            nums.popleft()
                            removed+=1
                        else:
                            removed=3
                    removing()
        removing()
        return totalOparation
    
slt = Solution()
print(slt.minimumOperations([1,2,3,4,2,3,3,5,7]))


