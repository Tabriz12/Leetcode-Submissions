class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not len(nums): return []
        start = nums[0]

        rolling = start

        out_list = []

        for idx, el in enumerate(nums[1:], 1):
            
            if nums[idx-1] + 1 == el:
                rolling = el
            
            else:
                if start < rolling:
                    out_list.append(f'{start}->{rolling}')
                else: out_list.append(f'{start}')
                start = el
                rolling = el
        
        if start < rolling:
            out_list.append(f'{start}->{rolling}')
        else: out_list.append(f'{start}')
        
        return(out_list)



        
