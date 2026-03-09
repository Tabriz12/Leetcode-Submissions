class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:


        tot = 0
        prev = None
        for row in bank:

            ones = row.count("1")


            if not ones:
                continue

            if not prev:

                prev = ones
            
            else:

                tot += prev * ones

                prev = ones
        

        return tot

                
        
