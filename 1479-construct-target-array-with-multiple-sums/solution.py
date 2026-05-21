class Solution:
    def isPossible(self, target: List[int]) -> bool:
        """
        Determine if we can transform an array of all 1s to the target array.
        In each operation, we can replace one element with the sum of all elements.
      
        Working backwards: the largest element must have been formed by summing all others.
        So we reverse the operation by subtracting the sum of others from the largest.
        """
        # Calculate total sum of all elements
        total_sum = sum(target)
      
        # Create max heap (negate values since Python has min heap by default)
        max_heap = [-num for num in target]
        heapify(max_heap)
      
        # Keep reducing the largest element until all elements become 1
        while -max_heap[0] > 1:
            # Get the current maximum element
            current_max = -heappop(max_heap)
          
            # Calculate sum of all other elements
            sum_of_others = total_sum - current_max
          
            # Edge cases where transformation is impossible
            if sum_of_others == 0 or current_max - sum_of_others < 1:
                return False
          
            # Calculate the previous value before this element became current_max
            # Use modulo for optimization when current_max >> sum_of_others
            # If remainder is 0, the previous value was sum_of_others
            previous_value = (current_max % sum_of_others) or sum_of_others
          
            # Push the previous value back to heap
            heappush(max_heap, -previous_value)
          
            # Update total sum
            total_sum = total_sum - current_max + previous_value
      
        # All elements are now 1, transformation is possible
        return True
        
