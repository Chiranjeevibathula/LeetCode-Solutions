from typing import List, Optional


class Trie:
    """A trie (prefix tree) data structure for efficient string storage and retrieval."""
  
    def __init__(self):
        # Array to store 26 child nodes (one for each lowercase letter)
        self.children: List[Optional[Trie]] = [None] * 26
        # Flag to mark if current node represents end of a word
        self.is_end: bool = False
  
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
      
        Args:
            word: The word to insert into the trie
        """
        current_node = self
      
        # Traverse through each character in the word
        for char in word:
            # Calculate index for the character (0-25 for a-z)
            index = ord(char) - ord('a')
          
            # Create new node if path doesn't exist
            if current_node.children[index] is None:
                current_node.children[index] = Trie()
          
            # Move to the child node
            current_node = current_node.children[index]
      
        # Mark the last node as end of word
        current_node.is_end = True
  
    def search(self, word: str) -> bool:
        """
        Check if a word can be built character by character where each prefix is also a word.
      
        Args:
            word: The word to search for
          
        Returns:
            True if word exists and all its prefixes are valid words, False otherwise
        """
        current_node = self
      
        # Traverse through each character in the word
        for char in word:
            # Calculate index for the character
            index = ord(char) - ord('a')
          
            # If path doesn't exist, word cannot be formed
            if current_node.children[index] is None:
                return False
          
            # Move to the child node
            current_node = current_node.children[index]
          
            # Check if current prefix is a valid word
            # Every prefix must be a valid word for the word to be buildable
            if not current_node.is_end:
                return False
      
        return True


class Solution:
    """Solution for finding the longest word that can be built one character at a time."""
  
    def longestWord(self, words: List[str]) -> str:
        """
        Find the longest word that can be built one character at a time from other words.
      
        Args:
            words: List of words to process
          
        Returns:
            The longest word that can be built progressively; 
            if tie, returns the lexicographically smallest one
        """
        # Build trie with all words
        trie = Trie()
        for word in words:
            trie.insert(word)
      
        # Track the best answer found so far
        longest_word = ""
      
        # Check each word to see if it can be built progressively
        for word in words:
            # Check if word can be built and if it's better than current answer
            if trie.search(word):
                # Update answer if current word is longer,
                # or same length but lexicographically smaller
                if (len(longest_word) < len(word) or 
                    (len(longest_word) == len(word) and longest_word > word)):
                    longest_word = word
      
        return longest_word
