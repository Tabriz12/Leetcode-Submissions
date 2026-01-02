from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:


        students = deque(students)

        sandwiches = deque(sandwiches)
        
        no_eat = 0

        while sandwiches:

            if no_eat == len(sandwiches):
                break

            if sandwiches[0] == students[0]:
                sandwiches.popleft()
                students.popleft()
                no_eat = 0
            
            else:

                students.rotate(-1)

                no_eat+=1
        
        return len(sandwiches)

            



        
