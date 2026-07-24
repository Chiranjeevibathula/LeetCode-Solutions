class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary mapping Roman numerals to their integer values
        roman_to_value = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
      
        # Import pairwise from itertools (Python 3.10+)
        from itertools import pairwise
      
        # Calculate the sum by iterating through consecutive pairs
        # If current value is less than next value, subtract it (e.g., IV = 4)
        # Otherwise, add it to the total
        result = sum(
            (-1 if roman_to_value[current] < roman_to_value[next_char] else 1) * roman_to_value[current] 
            for current, next_char in pairwise(s)
        )
      
        # Add the value of the last character (it's always added, never subtracted)
        result += roman_to_value[s[-1]]
      
        return result

