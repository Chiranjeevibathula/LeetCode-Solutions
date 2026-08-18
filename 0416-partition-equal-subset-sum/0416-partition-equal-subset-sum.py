class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        target,remainder=divmod(total,2)
        if remainder!=0:
            return False
        n=len(nums)
        dp=[[False]*(total+1) for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            current_sum=nums[i-1]
            for j in range(target+1):
                dp[i][j]=dp[i-1][j]
                if j>=current_sum:
                    dp[i][j]=dp[i][j] or dp[i-1][j-current_sum]
        return dp[n][target]            

        