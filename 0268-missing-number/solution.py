class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total_sum=n*(n+1)//2
        given_sum=sum(nums)
        ans=total_sum-given_sum
        return ans
        
