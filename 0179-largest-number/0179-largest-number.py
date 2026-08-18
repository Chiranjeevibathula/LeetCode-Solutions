from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str=[str(num) for num in nums]
        def compare(a:str,b:str)->int:
            if a+b<b+a:
                return 1
            else:
                return -1
        nums_str.sort(key=cmp_to_key(compare))
        if nums_str[0]=="0":
            return "0"
        return "".join(nums_str)                
        