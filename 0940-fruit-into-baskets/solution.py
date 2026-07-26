class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary to count frequency of each fruit type in current window
        fruit_count = Counter()
      
        # Initialize result and left pointer of sliding window
        max_fruits = 0
        left = 0
      
        # Iterate through fruits array with right pointer
        for right, fruit_type in enumerate(fruits):
            # Add current fruit to the window
            fruit_count[fruit_type] += 1
          
            # Shrink window from left if we have more than 2 fruit types
            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
              
                # Remove fruit type from counter if count becomes 0
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
              
                left += 1
          
            # Update maximum fruits collected (window size)
            max_fruits = max(max_fruits, right - left + 1)
      
        return max_fruits
