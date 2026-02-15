class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Shuffles an array by interleaving elements from two halves.
      
        Given an array of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn],
        returns the array in the form [x1,y1,x2,y2,...,xn,yn].
      
        Args:
            nums: List of integers with length 2n
            n: Integer representing half the length of nums
          
        Returns:
            List of integers with elements interleaved from two halves
        """
        # Split the array into two halves: first n elements and last n elements
        first_half = nums[:n]
        second_half = nums[n:]
      
        # Zip the two halves to create pairs (x1,y1), (x2,y2), ..., (xn,yn)
        # Then flatten each pair into the result list using list comprehension
        # The inner loop 'for x in pair' unpacks each tuple from zip
        result = [element for pair in zip(first_half, second_half) for element in pair]
      
        return result
        
