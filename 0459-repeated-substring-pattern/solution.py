from collections import deque
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # if s has n copies inside then s = c * n
        # c is child n is number of copies
        # if s * 2 then 2*n child
        # from s*2 if we remove first and last chars
        # 2(n-1) copies

        return s in (s*2)[1:-1]







