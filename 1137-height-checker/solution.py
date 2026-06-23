class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h=heights.copy()
        h.sort()
        n=len(heights)
        count=0        
        for i in range(n):
            if heights[i]!=h[i]:
                count+=1
        return count
               
        
