class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        running_sum = list(accumulate(nums))
        return running_sum
