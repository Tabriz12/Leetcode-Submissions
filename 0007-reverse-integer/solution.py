class Solution:
    def reverse(self, x: int) -> int:

        res = 0
        sign = -1 if x < 0 else 1
        for p, c in enumerate(str(abs(x))):

            if c != "0":

                res = res + int(c) * (10 ** p)
        
        if res > 2 ** 31 - 1:
            return 0
            
        return res * sign
        


            
        
