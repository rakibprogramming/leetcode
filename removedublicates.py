from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = []
        currentChecking = None
        while head:
            print(head)
            head = head.next
            # if currentChecking != i:
            #     newList.append(i)
            # currentChecking = i

        return newList
    
slt = Solution()
print(slt.deleteDuplicates([1,1,2,3,3]))