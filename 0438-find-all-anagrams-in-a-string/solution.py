class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length, p_length = len(s), len(p)
        result = []
      
        # Early return if s is shorter than p
        if s_length < p_length:
            return result
      
        # Counter for pattern p's character frequencies
        pattern_counter = Counter(p)
      
        # Initialize window counter with first (p_length - 1) characters of s
        window_counter = Counter(s[:p_length - 1])
      
        # Slide the window through string s
        for i in range(p_length - 1, s_length):
            # Add the rightmost character to the window
            window_counter[s[i]] += 1
          
            # Check if current window is an anagram of p
            if pattern_counter == window_counter:
                # Add the starting index of this window
                result.append(i - p_length + 1)
          
            # Remove the leftmost character from the window
            # Prepare for next iteration
            left_char = s[i - p_length + 1]
            window_counter[left_char] -= 1
          
            # Remove the character from counter if its count becomes 0
            if window_counter[left_char] == 0:
                del window_counter[left_char]
      
        return result
        
