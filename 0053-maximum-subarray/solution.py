class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=current_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(current_sum,0)+num
            max_sum=max(max_sum,current_sum)
        return max_sum    
        
