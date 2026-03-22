from copy import deepcopy
from collections import deque
class Solution:


    def rotate(self, row: list)->list:

        res = []

        order = deque()

        for el in row:

            if el == "#":
                order.append(el)
            
            elif el == ".":
                order.appendleft(el)
            
            else:

                res.extend(order)
                order = deque()
                res.append(el)
                    
        res.extend(order)
        return res


            



    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        r = len(boxGrid)
        c = len(boxGrid[0])

        res = [[0]*r for _ in range(c)]

        totrows = len(boxGrid)

        for rown, row in enumerate(boxGrid):

            col = self.rotate(row)
            coln = totrows-1-rown
            for idx, el in enumerate(col):

                res[idx][coln] = el
        

        return res

                






        



        
