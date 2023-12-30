class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2: return len(s)

        sub_dic = {}
        sub_dic[s[0]] = 0

        start = 0
        end = 1

        max_str = s[0]
        cur_str = s[0]

        while end < len(s):
            
            if s[end] not in sub_dic.keys() or sub_dic[s[end]] < start:

                sub_dic[s[end]] = end

                cur_str+=s[end]

                end+=1
            
            else:
                start = sub_dic[s[end]]+1
                sub_dic[s[end]] = end
                end+=1
                cur_str = s[start:end]
            
            if len(cur_str)>len(max_str): max_str=cur_str
        
        return len(max_str)
                    
            



            



        
