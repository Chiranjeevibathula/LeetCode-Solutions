from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        """
        Determine if Player 1 can win the game.
      
        Args:
            nums: List of non-negative integers representing scores
          
        Returns:
            True if Player 1 can win or tie, False otherwise
        """
      
        @cache
        def dfs(left: int, right: int) -> int:
            """
            Calculate the maximum score difference the current player can achieve
            over their opponent from nums[left] to nums[right].
          
            Args:
                left: Left boundary index of the subarray
                right: Right boundary index of the subarray
              
            Returns:
                Maximum score difference (current player's score - opponent's score)
            """
            # Base case: no elements left to pick
            if left > right:
                return 0
          
            # Current player chooses between:
            # 1. Pick nums[left] and let opponent play optimally on remaining array
            # 2. Pick nums[right] and let opponent play optimally on remaining array
            # The opponent's optimal play is subtracted since they try to maximize their own score
            pick_left = nums[left] - dfs(left + 1, right)
            pick_right = nums[right] - dfs(left, right - 1)
          
            # Return the maximum score difference achievable
            return max(pick_left, pick_right)
      
        # Player 1 wins if their score difference is non-negative
        return dfs(0, len(nums) - 1) >= 0


        
