class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_string=s+s
        first_occurance_start=doubled_string.index(s,1)
        return first_occurance_start<len(s)


        
