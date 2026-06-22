class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeros to the end of the array while maintaining
        the relative order of non-zero elements.
        Modifies the array in-place.

        Args:
            nums: List of integers to be modified in-place
        """
        # Pointer to track the position where next non-zero element should be placed
        non_zero_position = 0

        # Iterate through each element in the array
        for current_index, current_value in enumerate(nums):
            # If current element is non-zero
            if current_value != 0:
                # Swap current non-zero element with element at non_zero_position
                nums[non_zero_position], nums[current_index] = nums[current_index], nums[non_zero_position]
                # Move the non-zero position pointer forward
                non_zero_position += 1
