class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Find the number of ways to assign + or - signs to elements in nums to get target sum.
      
        This problem can be transformed into a subset sum problem:
        Let P be the sum of numbers with + sign, N be the sum of numbers with - sign
        P - N = target and P + N = sum(nums)
        Therefore: 2*N = sum(nums) - target, so N = (sum(nums) - target) / 2
      
        The problem becomes: find number of subsets with sum equal to N
        """
        total_sum = sum(nums)
      
        # Check if it's possible to achieve the target
        # 1. The absolute target cannot exceed total sum
        # 2. (total_sum - target) must be even to have an integer N
        if total_sum < abs(target) or (total_sum - target) % 2 != 0:
            return 0
      
        # Calculate the target sum for the negative subset
        num_elements = len(nums)
        negative_target = (total_sum - target) // 2
      
        # dp[i][j] represents number of ways to select from first i elements 
        # to get sum j
        dp = [[0] * (negative_target + 1) for _ in range(num_elements + 1)]
      
        # Base case: empty subset has sum 0, there's one way to achieve it
        dp[0][0] = 1
      
        # Fill the DP table
        for i in range(1, num_elements + 1):
            current_num = nums[i - 1]  # Current number (0-indexed in nums)
          
            for j in range(negative_target + 1):
                # Option 1: Don't include current number
                dp[i][j] = dp[i - 1][j]
              
                # Option 2: Include current number (if possible)
                if j >= current_num:
                    dp[i][j] += dp[i - 1][j - current_num]
      
        return dp[num_elements][negative_target]
