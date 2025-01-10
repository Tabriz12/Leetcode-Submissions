class Solution:
    def isHappy(self, n: int) -> bool:

        seeyou = set()

        def slice_and_dice(numb: int):
            result = 0
            while numb > 0:

                reminder = numb % 10

                result += reminder*reminder

                numb = numb // 10
            
            return result
        

        while n != 1:

            n = slice_and_dice(n)

            if n in seeyou:
                return False
            
            else:
                seeyou.add(n)


        return True   


        



        
