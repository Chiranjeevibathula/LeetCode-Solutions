class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert an integer to Roman numeral representation.
      
        Args:
            num: Integer to convert (1 <= num <= 3999)
          
        Returns:
            String representation of the Roman numeral
        """
        # Define Roman numeral symbols and their corresponding values
        # Ordered from largest to smallest, including subtractive notation cases
        roman_symbols = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        decimal_values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
      
        # List to collect Roman numeral parts
        result = []
      
        # Iterate through each Roman symbol and its value
        for symbol, value in zip(roman_symbols, decimal_values):
            # Greedily subtract the largest possible value
            while num >= value:
                num -= value
                result.append(symbol)
      
        # Join all parts into final Roman numeral string
        return ''.join(result)
        
