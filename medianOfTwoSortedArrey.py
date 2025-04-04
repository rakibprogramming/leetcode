import heapq
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        marged = list(heapq.merge(nums1,nums2))

        numsLen = len(marged)
        median = None
        if numsLen%2 == 1:
            median = marged[int((numsLen-1)/2)]
        else:
            print(int(((numsLen)/2)-0.5), int(((numsLen)/2)))
            median = (marged[int(((numsLen)/2)-0.5)] + marged[int(((numsLen)/2))])/2

        return median
    
d= [1,2]
c=[]
print(Solution().findMedianSortedArrays(d,c))