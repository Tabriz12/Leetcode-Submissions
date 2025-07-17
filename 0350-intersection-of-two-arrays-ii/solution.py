from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        res = []

        for k, v in nums1.items():

            if k in nums2.keys():
                print(k)

                res.extend( min(nums1[k], nums2[k]) * [k])
                print(res)

        return res
        



        
        
