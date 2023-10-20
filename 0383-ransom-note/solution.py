from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = Counter(list(magazine))
        for key, value in Counter(list(ransomNote)).items():
            
            try:
                if magazine[key]<value: return False
            except: return False
    
        return True

        
        
