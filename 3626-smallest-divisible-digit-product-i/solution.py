class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        """
        Find the smallest number >= n whose digit product is divisible by t.
      
        Args:
            n: The starting number (minimum value to consider)
            t: The target divisor for the digit product
          
        Returns:
            The smallest number >= n whose digit product is divisible by t
        """
        from itertools import count
      
        # Iterate through all numbers starting from n
        for candidate in count(n):
            # Calculate the product of all digits
            digit_product = 1
            temp_num = candidate
          
            # Extract each digit and multiply them together
            while temp_num > 0:
                digit = temp_num % 10  # Get the last digit
                digit_product *= digit  # Multiply it to the product
                temp_num //= 10  # Remove the last digit
          
            # Check if the digit product is divisible by t
            if digit_product % t == 0:
                return candidate
