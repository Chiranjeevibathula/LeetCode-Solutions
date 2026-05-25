class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(left: int, right: int) -> int:
            """
            Performs quickselect to find the kth smallest element in nums[left:right+1].
            Uses partition to divide the array and recursively search the correct half.
            """
            # Base case: single element
            if left == right:
                return nums[left]
          
            # Initialize two pointers for partitioning
            i, j = left - 1, right + 1
          
            # Choose middle element as pivot
            pivot = nums[(left + right) >> 1]
          
            # Partition the array around the pivot
            while i < j:
                # Move i forward until we find an element >= pivot
                while True:
                    i += 1
                    if nums[i] >= pivot:
                        break
              
                # Move j backward until we find an element <= pivot
                while True:
                    j -= 1
                    if nums[j] <= pivot:
                        break
              
                # Swap elements if pointers haven't crossed
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
          
            # After partition, elements at indices <= j are <= pivot
            # elements at indices > j are >= pivot
          
            # Determine which partition contains the target_index
            if j < target_index:
                # Target is in the right partition
                return quickselect(j + 1, right)
            else:
                # Target is in the left partition (including j)
                return quickselect(left, j)
      
        # Convert kth largest to (n-k)th smallest for easier processing
        n = len(nums)
        target_index = n - k
      
        # Find and return the element at target_index position
        return quickselect(0, n - 1)
        
