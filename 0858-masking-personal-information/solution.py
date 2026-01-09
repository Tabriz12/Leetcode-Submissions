class Solution:
    def maskPII(self, s: str) -> str:

        if "@" in s:

            first_part = s.split("@")[0]

            first_part = first_part[0].lower() + 5*"*" + first_part[-1].lower()

            second_part = s.split("@")[1].lower()

            return first_part + "@" + second_part

        else:

            num = ""
            last_4 = 0
            for char in s[-1::-1]:

                if char.isdigit():
                    if last_4 < 4:
                        num = char + num
                        last_4+=1
                    else:
                        if (len(num) - 4) % 4 == 0:
                            num = "-" + num
                        num = "*" + num
            
            
            return num if len(num) == 12 else "+" + num



        
