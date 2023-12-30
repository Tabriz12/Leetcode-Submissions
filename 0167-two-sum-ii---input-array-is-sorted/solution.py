class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        reminder = {}

        for idx, el in enumerate(numbers,1):
            if target-el in reminder.keys():
                return [reminder[target-el], idx]
            else: reminder[el] = idx
        
