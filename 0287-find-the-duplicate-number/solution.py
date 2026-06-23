class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Find the duplicate number using the binary search template.
        Feasible condition: count of numbers <= mid > mid
        """
        n = len(nums) - 1  # n is the max value (array has n+1 elements)

        # Binary search template on value range [1, n]
        left, right = 1, n
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2

            # Count how many numbers are <= mid
            count = sum(1 for num in nums if num <= mid)

            # Feasible: is there excess? (duplicate is <= mid)
            if count > mid:
                first_true_index = mid
                right = mid - 1  # Search for smaller duplicate
            else:
                left = mid + 1

        return first_true_index
