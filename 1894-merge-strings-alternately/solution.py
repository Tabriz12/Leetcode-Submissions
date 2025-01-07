class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        diff = len(word1) - len(word2)



        final = ""

        for i in range(min(len(word1), len(word2))):

            final+= word1[i] + word2[i]
        
        if diff>0:
            final += word1[i+1:]
        elif diff<0:
            final += word2[i+1:]
        
        return final



        
