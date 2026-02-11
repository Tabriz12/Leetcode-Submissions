class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        anchor = strs[0]
        
        ln = len(anchor)

        while ln > 0:
            found = False

            for strng in strs:

                if not strng.startswith(anchor[:ln]):

                    ln -=1
                    found = True
                    break
            
            if not found:
                break


            

                

            
            
        
        return anchor[:ln] if ln > 0 else ""




