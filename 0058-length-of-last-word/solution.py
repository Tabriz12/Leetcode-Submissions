class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([word.strip() for word in s.split()][-1])
        
