class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        from itertools import accumulate
        altitudes=accumulate(gain,initial=0)
        return max(altitudes)
        
