class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = Counter()
      
        # Left pointer of sliding window
        left = 0
      
        # Maximum frequency of any single character seen so far in any window
        max_freq = 0
      
        # Iterate through string with right pointer
        for right, char in enumerate(s):
            # Add current character to window
            char_count[char] += 1
          
            # Update maximum frequency
            # Note: max_freq may not be the max in current window, but that's okay
            # It helps maintain the largest valid window size found so far
            max_freq = max(max_freq, char_count[char])
          
            # Check if current window is invalid
            # Window is invalid if: (window_size - most_frequent_char_count) > k
            # This means we need more than k replacements
            if right - left + 1 - max_freq > k:
                # Shrink window from left
                char_count[s[left]] -= 1
                left += 1
      
        # The final window size is the answer
        # Since we only shrink when invalid, the window maintains max valid size
        return len(s) - left

        
