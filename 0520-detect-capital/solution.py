class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        return (word[1:].islower() or word.isupper() or len(word) == 1)

        
