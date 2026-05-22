class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # Calculate initial sums of elements at even and odd indices
        even_sum = sum(nums[::2])  # Sum of elements at even indices (0, 2, 4, ...)
        odd_sum = sum(nums[1::2])   # Sum of elements at odd indices (1, 3, 5, ...)
      
        # Initialize counters
        fair_count = 0  # Count of indices that make the array fair when removed
        left_even_sum = 0  # Sum of even-indexed elements to the left of current position
        left_odd_sum = 0   # Sum of odd-indexed elements to the left of current position
      
        # Iterate through each index to check if removing it makes the array fair
        for index, value in enumerate(nums):
            # When we remove an element at index i:
            # - Elements before i keep their parity (even/odd position)
            # - Elements after i switch their parity (even becomes odd, odd becomes even)
          
            if index % 2 == 0:  # Current element is at an even index
                # After removal: 
                # new_even_sum = left_even_sum + (odd_sum - left_odd_sum)
                # new_odd_sum = left_odd_sum + (even_sum - left_even_sum - value)
                if left_odd_sum + even_sum - left_even_sum - value == left_even_sum + odd_sum - left_odd_sum:
                    fair_count += 1
                left_even_sum += value
            else:  # Current element is at an odd index
                # After removal:
                # new_even_sum = left_even_sum + (odd_sum - left_odd_sum - value)
                # new_odd_sum = left_odd_sum + (even_sum - left_even_sum)
                if left_odd_sum + even_sum - left_even_sum == left_even_sum + odd_sum - left_odd_sum - value:
                    fair_count += 1
                left_odd_sum += value
      
        return fair_count
        
