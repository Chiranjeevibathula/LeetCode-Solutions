class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Find all numbers in range [1, n] that don't appear in the array.
      
        Args:
            nums: List of integers where n is the length of the array
      
        Returns:
            List of integers that are missing from the range [1, n]
        """
        # Convert the input list to a set for O(1) lookup time
        numbers_present = set(nums)
      
        # Build result list by checking each number in range [1, n]
        # If a number is not in the set, it's missing from the original array
        missing_numbers = [
            number 
            for number in range(1, len(nums) + 1) 
            if number not in numbers_present
        ]
      
        return missing_numbers
        
