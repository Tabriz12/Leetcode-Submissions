class Solution:


    def binario(self, l, u, n):

        while l < u:

            mid = (l + u) // 2

            if 2**mid == n:
                return True
            
            elif 2**mid > n:
                u = mid
            
            else:
                l = mid + 1
        
        return False

    def isPowerOfTwo(self, n: int) -> bool:

        if n < 1:
            return False
        
        elif n == 1:
            return True
        
        else:

            upper = 1

            while 2**upper<= n:

                if 2**upper == n:
                    return True
                
                else:
                    upper*=2
            
            return self.binario(upper// 2, upper, n)

            


        
