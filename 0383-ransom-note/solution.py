from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hash1 = Counter(ransomNote)
        hash2 = Counter(magazine)

        for k, v in hash1.items():

            if k in hash2.keys():
                if hash2[k] < v: return False
            
            else: return False
        
        return True


        
