class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind_s = 0
        ind_t = 0

        if len(s) == 0:
            return True

        while (ind_s < len(s)) and (ind_t < len(t)):
            if s[ind_s] == t[ind_t]:
                ind_s += 1
                ind_t += 1
            else:
                ind_t+=1
        

        return ind_s == len(s)
