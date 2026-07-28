class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start:int,end:int)->None:
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1        
        n=len(nums)
        k = k % n
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)        
        
