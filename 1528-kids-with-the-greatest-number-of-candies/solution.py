class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result=[]
        r=[]
        n=len(candies)
        for candy in candies:
            a=candy+extraCandies
            r.append(a)
        for i in range(n):
            if r[i]<max(candies):
                result.append(False)
            else:
                result.append(True)  
        return result          


        
