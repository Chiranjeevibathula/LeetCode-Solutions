class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def find_left_boundaries(max_distinct):
            """
            For each index i, find the leftmost index j such that 
            nums[j:i+1] contains at most max_distinct distinct integers.
          
            Returns a list where left_boundaries[i] represents the leftmost 
            valid starting position for subarrays ending at index i.
            """
            left_boundaries = [0] * len(nums)
            frequency_map = Counter()
            left_pointer = 0
          
            for right_pointer, current_num in enumerate(nums):
                # Add current element to the window
                frequency_map[current_num] += 1
              
                # Shrink window from left while we have too many distinct elements
                while len(frequency_map) > max_distinct:
                    left_num = nums[left_pointer]
                    frequency_map[left_num] -= 1
                  
                    # Remove element from map if its count reaches 0
                    if frequency_map[left_num] == 0:
                        del frequency_map[left_num]
                  
                    left_pointer += 1
              
                # Store the leftmost valid position for current right_pointer
                left_boundaries[right_pointer] = left_pointer
          
            return left_boundaries
      
        # Get left boundaries for at most (k-1) and at most k distinct elements
        boundaries_k_minus_1 = find_left_boundaries(k - 1)
        boundaries_k = find_left_boundaries(k)
      
        # The difference gives us the count of subarrays with exactly k distinct
        # For each position i, boundaries_k_minus_1[i] - boundaries_k[i] gives
        # the number of valid starting positions for subarrays ending at i
        # that have exactly k distinct integers
        return sum(left_k_minus_1 - left_k 
                   for left_k_minus_1, left_k in zip(boundaries_k_minus_1, boundaries_k))
