class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        idx = 0

        for char in s:
        
            try:
                t = t[idx:]
                idx = t.index(char) + 1
                

            except:
                return False
        
        return True

        
