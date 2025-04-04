from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sumpUP = 0
        for i in range(len(digits)):
            sumpUP+=digits[i]*(10**(len(digits)-(i+1)))

        addedNumber = sumpUP+1
        addedNumberList = list(str(addedNumber))
        addedNumberListInt = []
        for i in addedNumberList:
            addedNumberListInt.append(int(i))
        return addedNumberListInt