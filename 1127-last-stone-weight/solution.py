from collections import deque
class Solution:

    def _binario(self, val: int, queue):

        left = 0
        right = len(queue)

        while left < right:
            mid = (left + right) // 2

            if queue[mid] == val:
                return mid

            elif queue[mid] < val:

                left = mid + 1
            else:
                right = mid

        return left

        

        

    def lastStoneWeight(self, stones: List[int]) -> int:

        queue = deque(sorted(stones))

        while len(queue) > 1:

            collision = queue.pop() - queue.pop()

            idx = self._binario(collision, queue)
            
            queue.insert(idx, collision)

        
        return sum(queue)




    
        
