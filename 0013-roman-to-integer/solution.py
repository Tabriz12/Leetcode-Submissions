class Solution:
    def romanToInt(self, s: str) -> int:

        romans =  ['I', 'V', 'X', 'L', 'C', 'D', 'M' ]
        values = [1, 5, 10, 50, 100, 500, 1000]

        dic = dict(zip(romans, values))

        maxval = 0
        res = 0



        for ch in s[::-1]:

            if dic[ch]>=maxval:
                maxval = dic[ch]
                res+= dic[ch]
            else: res-= dic[ch]
        
        return res

            
            

        
