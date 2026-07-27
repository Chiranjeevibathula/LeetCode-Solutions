class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_prefix=0
        max_prefix=-float('inf')
        min_subarray_sum=float(inf)
        current_sum=0
        max_subarray_sum=float(-inf) 
        for num in nums:
            current_sum+=num
            max_subarray_sum=max(max_subarray_sum,current_sum-min_prefix)
            min_subarray_sum=min(min_subarray_sum,current_sum-max_prefix)
            max_prefix=max(max_prefix,current_sum)
            min_prefix=min(min_prefix,current_sum)
        return max(max_subarray_sum,current_sum-min_subarray_sum)    

