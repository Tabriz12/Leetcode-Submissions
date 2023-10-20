class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        

        res = -1
        step = len(needle)


        for idx in range(0, len(haystack)- len(needle)+1):
            if haystack[idx:idx+step] == needle:
                res = idx
                break
        
        return res
        
