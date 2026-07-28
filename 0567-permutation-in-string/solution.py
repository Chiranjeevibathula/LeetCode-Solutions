class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Count frequency of each character in s1
        char_count = Counter(s1)
        # Number of unique characters that still need to be matched
        chars_needed = len(char_count)
        # Length of the target string s1 (window size)
        window_size = len(s1)
      
        # Iterate through each character in s2
        for index, char in enumerate(s2):
            # Add current character to window by decreasing its required count
            char_count[char] -= 1
            # If this character's count reaches exactly 0, one less character type is needed
            if char_count[char] == 0:
                chars_needed -= 1
          
            # If window size exceeds s1 length, remove the leftmost character
            if index >= window_size:
                left_char = s2[index - window_size]
                # Remove leftmost character from window by increasing its count
                char_count[left_char] += 1
                # If this character's count becomes 1 (was 0), we need this character again
                if char_count[left_char] == 1:
                    chars_needed += 1
          
            # If all character requirements are met, permutation found
            if chars_needed == 0:
                return True
      
        # No permutation of s1 found in s2
        return False
        
