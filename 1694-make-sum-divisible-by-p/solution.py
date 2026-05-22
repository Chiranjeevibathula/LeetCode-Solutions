class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Calculate the remainder of the total sum divided by p
        # This is what we need to remove to make the remaining sum divisible by p
        total_remainder = sum(nums) % p
      
        # If the total sum is already divisible by p, no subarray needs to be removed
        if total_remainder == 0:
            return 0
      
        # Dictionary to store the last index where each prefix sum modulo p occurred
        # Initialize with 0: -1 to handle cases where the subarray starts from index 0
        last_seen_index = {0: -1}
      
        # Current prefix sum modulo p
        current_prefix_sum = 0
      
        # Initialize the answer to the length of the array (worst case)
        min_length = len(nums)
      
        # Iterate through each element in the array
        for index, num in enumerate(nums):
            # Update the current prefix sum modulo p
            current_prefix_sum = (current_prefix_sum + num) % p
          
            # Calculate the target prefix sum we're looking for
            # We need to find a previous prefix sum such that:
            # (current_prefix_sum - previous_prefix_sum) % p == total_remainder
            # This means: previous_prefix_sum == (current_prefix_sum - total_remainder) % p
            target_prefix_sum = (current_prefix_sum - total_remainder + p) % p
          
            # If we've seen this target prefix sum before, we can remove the subarray
            # between that previous index and the current index
            if target_prefix_sum in last_seen_index:
                subarray_length = index - last_seen_index[target_prefix_sum]
                min_length = min(min_length, subarray_length)
          
            # Update the last seen index for the current prefix sum
            last_seen_index[current_prefix_sum] = index
      
        # If min_length equals the array length, we can't remove the entire array
        # Return -1 in this case, otherwise return the minimum subarray length
        return -1 if min_length == len(nums) else min_length
        
