class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Find the duplicate number and the missing number in an array.
      
        The array should contain numbers from 1 to n, but one number appears twice
        and another number is missing.
      
        Args:
            nums: List of integers from 1 to n with one duplicate and one missing
          
        Returns:
            List containing [duplicate_number, missing_number]
        """
        n = len(nums)
      
        # Calculate the expected sum of numbers from 1 to n using arithmetic series formula
        expected_sum = (1 + n) * n // 2
      
        # Calculate the sum of unique numbers in the array (removes the duplicate)
        unique_sum = sum(set(nums))
      
        # Calculate the actual sum of all numbers in the array (includes the duplicate)
        actual_sum = sum(nums)
      
        # The duplicate number = actual_sum - unique_sum
        duplicate_number = actual_sum - unique_sum
      
        # The missing number = expected_sum - unique_sum
        missing_number = expected_sum - unique_sum
      
        return [duplicate_number, missing_number]
        
