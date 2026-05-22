class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index={}
        for index,num in enumerate(nums):
            compliment=target-num
            if compliment in nums_to_index:
                return [nums_to_index[compliment],index]
            nums_to_index[num]=index
        
