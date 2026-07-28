class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Count frequency of each character in target string t
        target_freq = Counter(t)
      
        # Track frequency of characters in current window
        window_freq = Counter()
      
        # Count of characters in window that match required frequency
        matched_chars = 0
      
        # Left pointer of sliding window
        left = 0
      
        # Track the start index and length of minimum window found
        min_start = -1
        min_length = inf
      
        # Expand window by moving right pointer
        for right, char in enumerate(s):
            # Add current character to window
            window_freq[char] += 1
          
            # Check if this character contributes to matching t
            if char in target_freq and window_freq[char] <= target_freq[char]:
                matched_chars += 1
          
            # Contract window when all characters from t are matched
            while matched_chars == len(t):
                # Update minimum window if current window is smaller
                current_window_size = right - left + 1
                if current_window_size < min_length:
                    min_length = current_window_size
                    min_start = left
              
                # Remove leftmost character from window
                left_char = s[left]
                if left_char in target_freq and window_freq[left_char] <= target_freq[left_char]:
                    matched_chars -= 1
                window_freq[left_char] -= 1
              
                # Move left pointer to contract window
                left += 1
      
        # Return empty string if no valid window found, otherwise return minimum window
        return "" if min_start == -1 else s[min_start : min_start + min_length]
