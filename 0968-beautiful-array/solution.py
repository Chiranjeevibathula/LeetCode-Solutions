class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n==1:
            return [1]
        left_half=self.beautifulArray((n+1)//2)
        right_half=self.beautifulArray(n//2) 
        odd_numbers=[x*2-1 for x in left_half]
        even_numbers=[x*2 for x in right_half]
        return odd_numbers+even_numbers  
        
