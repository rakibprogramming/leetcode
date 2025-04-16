from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        print(nums)
        subset = []
        for b in range(len(nums)):
            tempSubset = [nums[b]]

            for i in range(len(nums)):
                willBeAdd = False
                for cc in tempSubset:
                    if cc == nums[i]:
                        break
                    if cc % nums[i] == 0 or nums[i] % cc == 0:
                        willBeAdd = True
                        pass
                    else:
                        willBeAdd = False
                        break
                if willBeAdd:
                    tempSubset.append(nums[i])
            print(tempSubset)
            if len(tempSubset) > len(subset):
                subset = tempSubset[:]

        return subset


slt = Solution()
print(slt.largestDivisibleSubset([5,9,18,54,108,540,90,180,360,720]))