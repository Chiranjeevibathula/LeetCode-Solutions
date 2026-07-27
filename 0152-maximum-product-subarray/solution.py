class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product=max_ending_here=min_ending_here=nums[0]
        for num in nums[1:]:
            prev_max=max_ending_here
            prev_min=min_ending_here
            max_ending_here=max(num,prev_max*num,prev_min*num)
            min_ending_here=min(num,prev_max*num,prev_min*num)
            max_product=max(max_product,max_ending_here)
        return max_product
        
