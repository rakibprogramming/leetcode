class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ")
        length= 0
        for i in range(len(arr)):
            value = arr[(len(arr) - i)-1]
            if value != "":
                length = len(value)
                break

        return length