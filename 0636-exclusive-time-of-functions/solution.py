from collections import deque
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:

        stack = deque()
        idle_stack = deque()
        res = {}
        for log in logs:
            idx, event, ts = log.split(":")

            ts = int(ts)
            idx = int(idx)

            if event == 'start':


                stack.appendleft(ts)
                if idx not in res:
                    res[idx] = 0
                
                idle_stack.appendleft(0)

            else:
                end = ts
                start = stack.popleft()

                idle = idle_stack.popleft()
                diff = (end-start+1)- idle
                res[idx] += diff

                if stack:
                    last_idle = idle_stack.popleft() + (end-start+1)
                    idle_stack.appendleft(last_idle)
        
        return [res[i] for i in range(n)]

        
