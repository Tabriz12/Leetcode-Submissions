from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result  = [0] * len(temperatures)

        stack  = deque()

        stack.append(temperatures[-1])
        survivors = {temperatures[-1]: 0}

        for idx, temp in zip(range(len(temperatures)-2, -1, -1), temperatures[-2::-1]):
            cnt = 0
            while stack:
                stack_top = stack.pop()
                cnt+=1
                
                if temp >= stack_top:

                    cnt += survivors[stack_top]

                if temp < stack_top:
                    stack.append(stack_top)
                    stack.append(temp)
                    survivors[temp] = cnt - 1
                    result[idx] = cnt
                    break
            
            if not stack:
                stack.append(temp)
                survivors[temp] = 0
                
        return result



