class Solution:

    def preprocess(self, s: str):

        return "".join([c.lower() for c in list(s) if c.isalnum()])

    def isPalindrome(self, s: str) -> bool:

        clean = self.preprocess(s)
        
        if len(clean) < 2:
            return True
        
        
        mid = len(clean) // 2

        return clean[:mid] == clean[-1:-mid - 1:-1]
        

