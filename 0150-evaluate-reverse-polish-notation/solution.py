from collections import deque
from ast import literal_eval
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        for token in tokens:
            
            res = token

            try:
                int_token = int(token)
                stack.appendleft(token)
                
            except:
                
                second = stack.popleft()
                first = stack.popleft()
                
                res = eval(first + " " + token + " " + second)
                if token  == "/":
                    res = int(res)

                stack.appendleft(str(res))
        
        return int(res)





        
