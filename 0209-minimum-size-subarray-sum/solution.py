class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Get the length of the input array
        n = len(nums)

        # Create prefix sum array with initial value 0
        # prefix_sums[i] represents sum of nums[0:i]
        prefix_sums = list(accumulate(nums, initial=0))

        # Initialize minimum length to n+1 (impossible value)
        min_length = n + 1

        # Iterate through each position in prefix sum array
        for i in range(n + 1):
            # Binary search template to find first j where prefix_sums[j] >= prefix_sums[i] + target
            left, right = i, n
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if prefix_sums[mid] >= prefix_sums[i] + target:
                    first_true_index = mid
                    right = mid - 1
                else:
                    left = mid + 1

            # If valid position found, update minimum length
            if first_true_index != -1:
                min_length = min(min_length, first_true_index - i)

        # Return minimum length if found, otherwise return 0
        return min_length if min_length <= n else 0
        
