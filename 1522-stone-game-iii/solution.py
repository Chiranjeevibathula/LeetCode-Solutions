class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        from functools import cache
        from math import inf
      
        @cache
        def dfs(index: int) -> int:
            """
            Calculate the maximum score difference the current player can achieve
            starting from index position.
          
            Args:
                index: Current position in the stone array
              
            Returns:
                Maximum score difference (current player's score - opponent's score)
            """
            # Base case: no stones left
            if index >= n:
                return 0
          
            # Try taking 1, 2, or 3 stones and find the best outcome
            max_score_diff = -inf
            current_sum = 0
          
            for num_stones in range(3):
                # Check if we can take this many stones
                if index + num_stones >= n:
                    break
              
                # Add the stone value to current sum
                current_sum += stoneValue[index + num_stones]
              
                # Calculate score difference:
                # current_sum (what we take) - dfs(next) (opponent's best from remaining)
                score_diff = current_sum - dfs(index + num_stones + 1)
                max_score_diff = max(max_score_diff, score_diff)
          
            return max_score_diff
      
        # Initialize game parameters
        n = len(stoneValue)
      
        # Get Alice's maximum score difference
        alice_score_diff = dfs(0)
      
        # Determine winner based on score difference
        if alice_score_diff == 0:
            return 'Tie'
        elif alice_score_diff > 0:
            return 'Alice'
        else:
            return 'Bob'
