class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        epitaph = ""
        
        for ind in range(len(s)-1, -1, -1):

            if s[ind] != " ":

                epitaph =  s[ind] + epitaph
            
            else:
                if len(epitaph) > 0:
                    return len(epitaph)
        
        return len(epitaph)
            

            


        
