class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given array.
      
        Args:
            nums: List of integers
          
        Returns:
            List of all possible subsets
        """
      
        def backtrack(index: int) -> None:
            """
            Recursive helper function to generate subsets using backtracking.
          
            Args:
                index: Current index in the nums array
            """
            # Base case: reached the end of the array
            if index == len(nums):
                # Add a copy of current subset to the result
                result.append(current_subset[:])
                return
          
            # Choice 1: Exclude the current element
            backtrack(index + 1)
          
            # Choice 2: Include the current element
            current_subset.append(nums[index])
            backtrack(index + 1)
          
            # Backtrack: remove the element we just added
            current_subset.pop()
      
        # Initialize result list to store all subsets
        result = []
      
        # Initialize temporary list to build current subset
        current_subset = []
      
        # Start the backtracking process from index 0
        backtrack(0)
      
        return result
