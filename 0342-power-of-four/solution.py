class Solution:


    def binu(self, n, l=1, k=4):

        

        while n >= k**(2*l):

            l*=2
        
        r = l * 2

        while l < r:

            mid = (l+r)//2


            if k**mid == n:

                return True
            

            elif k**mid > n:

                r = mid
            
            else:
                l = mid + 1
            
        return False



    def isPowerOfFour(self, n: int) -> bool:

        k = 4
        if n<1:
            return False
        
        elif n==1:
            return True
        
        elif n < k:
            return False

        else:

            l = 1

            return self.binu(n, l, k)

        
