


class Solution:
    def romanToInt(self, s: str) -> int:
        
        values = {
            'I':1,   
            'V':5,   
            'X':10,  
            'L':50,  
            'C':100, 
            'D':500, 
            'M':1000,
        }



        romanNumberValue = s
        decimalNumberValue=0
        p=0
        while p < len(romanNumberValue):
                if values[romanNumberValue[p]] < values[(romanNumberValue+"M")[p+1]] and (romanNumberValue+":")[p+1] != ":":
                    decimalNumberValue+= values[romanNumberValue[p+1]] - values[romanNumberValue[p]]
                    p+=2
                else:
                    decimalNumberValue+= values[romanNumberValue[p]]
                    p+=1
            
        return decimalNumberValue
    

slt = Solution()
print(slt.romanToInt("IL"))