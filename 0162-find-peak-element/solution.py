class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        first_true_index = -1

        # Binary search using the template: find first index where nums[mid] > nums[mid + 1]
        while left <= right:
            mid = (left + right) // 2

            # Feasible condition: nums[mid] > nums[mid + 1]
            # For last element, treat as feasible (nums[n] = -infinity)
            if mid == n - 1 or nums[mid] > nums[mid + 1]:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        # first_true_index points to a peak element
        return first_true_index
