class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        

        final = ""

        for char in s[-1::-1]:

            if (len(final)+1) % (k+1) ==0:
                    final = "-" + final
            
            if char.isalnum():

                final = char.upper() + final

            
        return final[1:] if final and final[0] =="-" else final
        



        
