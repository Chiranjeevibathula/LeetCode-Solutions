class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
         # Track maximum sum subarray (Kadane's algorithm variant)
        max_sum = 0
        # Track minimum sum subarray (Kadane's algorithm variant)
        min_sum = 0
        # Track the maximum absolute sum found so far
        max_absolute = 0
      
        for num in nums:
            # Update max_sum: either extend current positive sum or start fresh from current number
            max_sum = max(max_sum, 0) + num
            # Update min_sum: either extend current negative sum or start fresh from current number
            min_sum = min(min_sum, 0) + num
            # Update answer with the maximum of current answer, max_sum, or absolute value of min_sum
            max_absolute = max(max_absolute, max_sum, abs(min_sum))
      
        return max_absolute
        
