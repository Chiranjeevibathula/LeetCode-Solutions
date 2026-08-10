class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_subsequence(nums: List[int], k: int) -> List[int]:
            """
            Extract the maximum subsequence of length k from nums while maintaining order.
            Uses a monotonic stack approach to greedily select largest elements.
            """
            n = len(nums)
            stack = [0] * k  # Pre-allocate stack of size k
            top = -1  # Stack pointer (top index)
            elements_to_drop = n - k  # Number of elements we can skip
          
            for num in nums:
                # Pop smaller elements from stack if we can still drop elements
                while top >= 0 and stack[top] < num and elements_to_drop > 0:
                    top -= 1
                    elements_to_drop -= 1
              
                # Add current element if stack not full
                if top + 1 < k:
                    top += 1
                    stack[top] = num
                else:
                    # Stack is full, just decrement elements_to_drop
                    elements_to_drop -= 1
          
            return stack
      
        def is_greater(nums1: List[int], nums2: List[int], idx1: int, idx2: int) -> bool:
            """
            Compare two arrays starting from given indices.
            Returns True if nums1[idx1:] is lexicographically greater than nums2[idx2:].
            """
            # If nums1 exhausted, it's not greater
            if idx1 >= len(nums1):
                return False
            # If nums2 exhausted but nums1 has elements, nums1 is greater
            if idx2 >= len(nums2):
                return True
            # Compare current elements
            if nums1[idx1] > nums2[idx2]:
                return True
            if nums1[idx1] < nums2[idx2]:
                return False
            # If equal, recursively compare next elements
            return is_greater(nums1, nums2, idx1 + 1, idx2 + 1)
      
        def merge_arrays(nums1: List[int], nums2: List[int]) -> List[int]:
            """
            Merge two arrays to create the maximum possible array.
            Always picks the lexicographically larger remaining portion.
            """
            m, n = len(nums1), len(nums2)
            idx1 = idx2 = 0
            result = [0] * (m + n)
          
            for pos in range(m + n):
                # Choose from nums1 if it has greater or equal remaining portion
                if is_greater(nums1, nums2, idx1, idx2):
                    result[pos] = nums1[idx1]
                    idx1 += 1
                else:
                    result[pos] = nums2[idx2]
                    idx2 += 1
          
            return result
      
        # Main logic
        m, n = len(nums1), len(nums2)
        # Determine valid range for elements to take from nums1
        min_from_nums1 = max(0, k - n)  # Must take at least k-n from nums1
        max_from_nums1 = min(k, m)      # Can take at most min(k, m) from nums1
      
        max_result = [0] * k
      
        # Try all valid splits between nums1 and nums2
        for take_from_nums1 in range(min_from_nums1, max_from_nums1 + 1):
            take_from_nums2 = k - take_from_nums1
          
            # Get maximum subsequences from each array
            subsequence1 = get_max_subsequence(nums1, take_from_nums1)
            subsequence2 = get_max_subsequence(nums2, take_from_nums2)
          
            # Merge the subsequences to get candidate result
            candidate = merge_arrays(subsequence1, subsequence2)
          
            # Update max_result if candidate is lexicographically larger
            if max_result < candidate:
                max_result = candidate
      
        return max_result
        