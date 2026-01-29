from math import sqrt, floor
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        for a in range(floor(sqrt(c)) + 1):


            if sqrt(c-a*a) == floor(sqrt(c-a*a)):
                return True
        
        return False

        
        
