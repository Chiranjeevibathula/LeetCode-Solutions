class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        Distribute minimum candies to children based on ratings.
        Each child must receive at least one candy.
        Children with higher ratings than neighbors must get more candies.
      
        Args:
            ratings: List of integers representing children's ratings
          
        Returns:
            Minimum number of candies needed
        """
        n = len(ratings)
      
        # Initialize arrays to track candy requirements from left and right traversals
        left_to_right = [1] * n  # Minimum candies needed considering left neighbor
        right_to_left = [1] * n  # Minimum candies needed considering right neighbor
      
        # Left to right pass: ensure each child with higher rating than left neighbor gets more candy
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_to_right[i] = left_to_right[i - 1] + 1
      
        # Right to left pass: ensure each child with higher rating than right neighbor gets more candy
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] = right_to_left[i + 1] + 1
      
        # Take maximum of both requirements at each position to satisfy both constraints
        total_candies = sum(max(left_candies, right_candies) 
                           for left_candies, right_candies in zip(left_to_right, right_to_left))
      
        return total_candies


