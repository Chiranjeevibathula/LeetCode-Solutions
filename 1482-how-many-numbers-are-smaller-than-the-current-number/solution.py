class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Create a sorted copy of the input array
        # This allows us to use binary search to find positions
        sorted_nums = sorted(nums)
      
        # For each number in the original array, find how many numbers are smaller
        # bisect_left returns the leftmost position where the number would be inserted
        # This position equals the count of numbers smaller than the current number
        result = [bisect_left(sorted_nums, num) for num in nums]
      
        return result

        
