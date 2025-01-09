class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        
        strs = sorted(strs)
        
        common = strs[0]

        for string in strs[1:]:

            if len(string) < len(common):

                if string == common[:len(string)]: 
                    common = string
                    print("case 1")
                    print(common)

                else:
                    for end in range(len(string)-1, -1, -1):
                        if string[:end] == common[:end]:
                            common = common[:end]
                            print("case 2")
                            print(common)
                            break
            else:
                if string[:len(common)] != common:
                    for end in range(len(common)-1, -1, -1):
                        if string[:end] == common[:end]:
                            common = common[:end]
                            print("case 3")
                            print(common)
                            break

            if len(common) == 0: return ""
        
        return common


            




                    








        
