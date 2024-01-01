class Solution:
    def intToRoman(self, num: int) -> str:

        romans = {1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
        }

        roman_text = ''

        digit = 0

        while num > 0:

            reminder = num % 10
            num = num // 10
            
            if reminder % 5 == 4:
                
                roman_text = romans[10**digit] + romans[(reminder+1)*(10**digit)] + roman_text
                
            else: 
                if reminder < 4:

                    roman_text = romans[10**digit] * reminder + roman_text
                
                else:

                    roman_text = romans[10**digit*5] + romans[10**digit] * (reminder - 5) + roman_text
            
            digit +=1
        
        return roman_text

                
                

            
            

            
        
