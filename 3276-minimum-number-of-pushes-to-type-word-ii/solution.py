from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count frequency of each character in the word
        char_frequency = Counter(word)
      
        # Initialize result variable to track total pushes needed
        total_pushes = 0
      
        # Sort frequencies in descending order to assign most frequent chars to keys requiring fewer pushes
        sorted_frequencies = sorted(char_frequency.values(), reverse=True)
      
        # Iterate through sorted frequencies with index
        for index, frequency in enumerate(sorted_frequencies):
            # Calculate number of pushes needed for this character:
            # - First 8 chars (index 0-7) need 1 push each
            # - Next 8 chars (index 8-15) need 2 pushes each
            # - Next 8 chars (index 16-23) need 3 pushes each, and so on
            pushes_per_char = (index // 8) + 1
          
            # Add total pushes for this character (pushes per occurrence * frequency)
            total_pushes += pushes_per_char * frequency
      
        return total_pushes
