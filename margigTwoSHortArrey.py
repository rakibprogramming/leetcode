
class Solution(object):
    def get_length(self,head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    def mergeTwoLists(self, a, b):
        print(a, b)
        c=[]
        locB=0
        locA=0

        for i in range(self.get_length(a)+self.get_length(b)):
            thisB = None
            thisA = None
            if locA < self.get_length(a):
                thisA = a[locA]
                locA+=1
            if locB < self.get_length(b):
                thisB = b[locB]
                locB+=1
            
            if thisA != None and thisB !=None:
                if thisA < thisB:
                    c.append(thisA)
                    locB-=1
                elif thisB < thisA:
                    c.append(thisB)
                    locA-=1
                elif thisB == thisA:
                    c.append(thisA)
                    c.append(thisB)
            elif not thisB and not thisA:
                break
            elif any([thisA,thisB]):
                lis = [thisA,thisB]
                c.append(max(x for x in lis if x is not None))

            print(thisA, thisB, (locA, locB))
        return c
    



