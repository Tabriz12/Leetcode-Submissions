class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        

        alt = max_alt = 0

        for n in gain:

            alt += n

            max_alt = max(max_alt, alt)
            
        return max_alt
