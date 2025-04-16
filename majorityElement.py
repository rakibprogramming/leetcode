from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        amount = {}
        for i in nums:
            if i in amount:
                amount[i] = amount[i] +1
            else:
                amount[i] = 1
        return max(amount, key=amount.get)
    

slt = Solution()
print(slt.majorityElement([2,2,1,1,1,2,2]))