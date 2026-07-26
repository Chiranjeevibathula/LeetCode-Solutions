class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize max heap with first k-1 elements
        # Use negative values to simulate max heap (Python has min heap by default)
        # Store tuples of (negative_value, index) to track element positions
        max_heap = [(-value, index) for index, value in enumerate(nums[:k - 1])]
        heapify(max_heap)
      
        # Result list to store maximum values of each window
        result = []
      
        # Slide the window from position k-1 to the end
        for i in range(k - 1, len(nums)):
            # Add current element to the heap
            heappush(max_heap, (-nums[i], i))
          
            # Remove elements that are outside the current window
            # The window's valid range is [i - k + 1, i]
            while max_heap[0][1] <= i - k:
                heappop(max_heap)
          
            # The maximum element is at the top of the heap
            # Convert back to positive value and add to result
            result.append(-max_heap[0][0])
      
        return result
        
