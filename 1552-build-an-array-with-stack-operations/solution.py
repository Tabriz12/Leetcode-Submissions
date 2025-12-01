
class Solution:

    
    def buildArray(self, target: List[int], n: int) -> List[str]:

        push = "Push"
        pop = "Pop"
        ops = []
        
        i = 1
        k = 0

        while (i <= n ) and (i <= target[-1]):
            if i == target[k]:
                ops.append("Push")
                i+=1
                k+=1
            
            else:
                ops.extend(["Push", "Pop"])
                i+=1
        
        return ops
            





        
        
