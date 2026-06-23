class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Reverse the order of words in a string.
      
        Args:
            s: Input string containing words separated by spaces
          
        Returns:
            String with words in reversed order, separated by single spaces
        """
        words = []
        i = 0
        n = len(s)
      
        # Iterate through the string to extract words
        while i < n:
            # Skip leading spaces
            while i < n and s[i] == " ":
                i += 1
          
            # Check if we've reached a word
            if i < n:
                # Mark the start of the word
                word_start = i
              
                # Find the end of the current word
                while i < n and s[i] != " ":
                    i += 1
              
                # Extract and store the word
                words.append(s[word_start:i])
      
        # Reverse the list of words and join them with single spaces
        return " ".join(words[::-1])
        
