class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        from functools import cache
        @cache
        def calculate_score_difference(left:int,right:int)->int:
            if left>right:
                return 0
            left_pick=piles[left]-calculate_score_difference(left+1,right)  
            right_pick=piles[right]-calculate_score_difference(left,right-1)  
            return max(left_pick,right_pick)
        return calculate_score_difference(0, len(piles) - 1) > 0    
        
