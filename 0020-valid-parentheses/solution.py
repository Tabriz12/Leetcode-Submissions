from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1: return False

        stack = deque()

        opening  = ["(", "{", "["]
        closing = [")", "}", "]"]

        dic = dict(zip(opening, closing))

        for char in s:
            if char in dic:

                stack.append(char)
            
            else:

                if not stack or dic[stack.pop()] != char: return False
        
        return True if not stack else False








        
