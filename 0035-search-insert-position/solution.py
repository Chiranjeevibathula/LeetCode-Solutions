class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        first_true_index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        # If first_true_index is -1, all elements are smaller than target
        # Insert at the end
        return first_true_index if first_true_index != -1 else n
        
