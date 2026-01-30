class Solution:


    def update_double(self, start):

        return start, start + 1, start + 1
    
    def update_single(self, start):

        return start + 1, start + 1, start + 1

    def check_pals(self, left, right, start, max_str, s, update_rule):

        while start < len(s):

            while (left >=0) and (right  < len(s)):

                if s[left] == s[right]:

                    max_str = s[left:right+1] if right-left + 1 > len(max_str) else max_str
                    left -= 1
                    right+= 1
                

                else:
                    left, right, start = update_rule(start)
            
            left, right, start = update_rule(start)
        
        return max_str



    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1: return s

        start = left = right = 0

        max_str = self.check_pals(left, right, start, "", s, self.update_single)

        
        start, left, right = 1, 0, 1

        return self.check_pals(left, right, start, max_str, s, self.update_double)





            





        

