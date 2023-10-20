class Solution:
    def climbStairs(self, n: int) -> int:
        
        ways =  [1, 2]

        if n < len(ways):
            return ways[n-1]
        else:
            for idx in range(len(ways),n):
                ways.append(ways[idx-1]+ways[idx-2])
        
        return ways[-1]

        
