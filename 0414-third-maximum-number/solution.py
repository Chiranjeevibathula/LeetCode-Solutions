class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Initialize three variables to track the top 3 maximum values
        # Use negative infinity as initial values to handle negative numbers
        first_max = second_max = third_max = float('-inf')
      
        # Iterate through each number in the array
        for num in nums:
            # Skip duplicates - we only want distinct maximum values
            if num in [first_max, second_max, third_max]:
                continue
          
            # Update the three maximum values based on current number
            if num > first_max:
                # New largest number found - shift all values down
                third_max, second_max, first_max = second_max, first_max, num
            elif num > second_max:
                # New second largest number found - shift second and third down
                third_max, second_max = second_max, num
            elif num > third_max:
                # New third largest number found - only update third
                third_max = num
      
        # Return third maximum if it exists, otherwise return the maximum
        # If third_max is still -inf, it means we have less than 3 distinct numbers
        return third_max if third_max != float('-inf') else first_max

        
        
