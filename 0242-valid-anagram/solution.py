from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        ct = Counter(t)
        cs = Counter(s)

        for k, v in cs.items():

            if k in ct.keys():
                if v != ct[k]: return False
            else: return False
        
        return True


        
