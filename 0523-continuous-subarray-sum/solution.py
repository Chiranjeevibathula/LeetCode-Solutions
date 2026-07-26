class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence index of each remainder
        # Initialize with remainder 0 at index -1 to handle edge cases
        remainder_to_index = {0: -1}
      
        # Running sum modulo k
        running_sum = 0
      
        # Iterate through the array with index and value
        for index, num in enumerate(nums):
            # Update running sum and take modulo k
            running_sum = (running_sum + num) % k
          
            # If this remainder hasn't been seen before, record its first occurrence
            if running_sum not in remainder_to_index:
                remainder_to_index[running_sum] = index
            # If remainder was seen before and subarray length is at least 2
            elif index - remainder_to_index[running_sum] > 1:
                # Found a valid subarray whose sum is divisible by k
                return True
      
        # No valid subarray found
        return False
