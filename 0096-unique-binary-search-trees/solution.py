class Solution:


    def __init__(self):

        self.cache = {0:1, 1:1}

    def solve(self, n):

        if n in self.cache:
            return self.cache[n]
        

        else:
            res = 0
            for i in range(1, n+1):


                left = self.solve(i-1)
                right = self.solve(n-i)

                res += left * right

                self.cache[n] = res
        
        return res




    def numTrees(self, n: int) -> int:

        return self.solve(n)
        
