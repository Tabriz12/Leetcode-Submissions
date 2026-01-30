class Solution:
    def myAtoi(self, s: str) -> int:

        digits = ""

        signs = {"+", "-"}

        sign = 0

        for char in s.strip():


            if char in signs and not digits and not sign:
                sign = 1 if char == "+" else -1
            
            elif char.isnumeric():
                digits+=char
            
            elif not char.isnumeric():
                break
        if not digits: return 0

        
        value = int(digits) if sign == 0 else int(digits) * sign

        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value


        
