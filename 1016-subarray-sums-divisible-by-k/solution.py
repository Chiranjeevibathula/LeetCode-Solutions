from typing import List
from collections import Counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store frequency of each remainder
        # Initialize with remainder 0 having count 1 (empty prefix)
        remainder_count = Counter({0: 1})
      
        # Initialize result counter and running prefix sum
        result = 0
        prefix_sum = 0
      
        # Iterate through each number in the array
        for num in nums:
            # Update prefix sum and get its remainder when divided by k
            # Using modulo to keep the remainder in range [0, k-1]
            prefix_sum = (prefix_sum + num) % k
          
            # If we've seen this remainder before, all previous occurrences
            # form valid subarrays with the current position
            result += remainder_count[prefix_sum]
          
            # Increment the count for current remainder
            remainder_count[prefix_sum] += 1
      
        return result

