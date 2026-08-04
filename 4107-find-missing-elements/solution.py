class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        nums.sort()
        for i in range(nums[0],nums[n-1]):
            if i not in nums:
                result.append(i)
        return result        
        
