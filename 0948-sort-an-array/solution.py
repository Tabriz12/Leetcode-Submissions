class Solution:

    def merge(self, left, right):

        ir = il = 0
        res = []
        while len(left) > il and len(right) > ir:

            if left[il] < right[ir]:

                res.append(left[il])
                il+=1
            
            else:

                res.append(right[ir])
                ir+=1
            
        
        res.extend(left[il:])
        res.extend(right[ir:])

        return res

    def divide(self, arr):
        
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2

        left_a = arr[:mid]
        right_a = arr[mid:]

        left = self.divide(left_a)
        right = self.divide(right_a)

        return self.merge(left, right)


    def sortArray(self, nums: List[int]) -> List[int]:

        return self.divide(nums)

        


        

