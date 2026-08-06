class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize write pointer to track position for unique elements
        write_index = 0
      
        # Iterate through each element in the array
        for current_num in nums:
            # Check if this is the first element or if current element is different from previous unique element
            if write_index == 0 or current_num != nums[write_index - 1]:
                # Place the unique element at the write position
                nums[write_index] = current_num
                # Move write pointer forward
                write_index += 1
      
        # Return the count of unique elements
        return write_index
