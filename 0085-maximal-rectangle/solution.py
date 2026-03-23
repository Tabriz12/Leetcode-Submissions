from collections import deque
class Solution:

    def monostack(self, row):

        stack = deque([])

        maxs = 0

        for i, n in enumerate(row):

            temp = i


            while stack and stack[-1][-1] > n:

                top_i, top_n = stack.pop()

                temp = top_i

                maxs = max(maxs, (i-top_i)*top_n)
            
            stack.append([temp, n])
        
        if stack:

            while stack:

                top_i, top_n = stack.pop()

                maxs = max(maxs, (len(row)-top_i)*top_n)
        
        
        return maxs
        



    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        n = len(matrix[0])
        height = [0] * n
        res = 0
        
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == "1" else 0
            
            
            res = max(res, self.monostack(height))
            
        return res



        
