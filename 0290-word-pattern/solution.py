class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        arr_pattern = list(pattern)
        arr_s = s.strip().split()

        if len(arr_pattern) != len(arr_s): return False
        
        return len(set(zip(arr_pattern, arr_s))) == len(set(arr_pattern)) == len(set(arr_s))

        
        
