from collections import Counter
from typing import Optional

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Get the length of the input string
        string_length = len(s)
      
        # Count frequency of each character
        char_frequency = Counter(s)
      
        # Find the maximum frequency among all characters
        max_frequency = max(char_frequency.values())
      
        # Check if reorganization is possible
        # If any character appears more than (n+1)/2 times, it's impossible
        # to arrange without having two adjacent same characters
        if max_frequency > (string_length + 1) // 2:
            return ''
      
        # Initialize result array with None values
        result = [None] * string_length
      
        # Start placing characters at even indices (0, 2, 4, ...)
        current_index = 0
      
        # Process characters in descending order of frequency
        # This ensures the most frequent character gets spread out first
        for character, frequency in char_frequency.most_common():
            # Place all occurrences of the current character
            while frequency > 0:
                # Place character at current position
                result[current_index] = character
                frequency -= 1
              
                # Move to next even index
                current_index += 2
              
                # If we've exhausted even indices, switch to odd indices (1, 3, 5, ...)
                if current_index >= string_length:
                    current_index = 1
      
        # Convert the result array to a string and return
        return ''.join(result)
