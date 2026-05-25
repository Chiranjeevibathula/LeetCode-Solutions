class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left,right=1,len(arr)-2
        first_occurance_index=-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]>arr[mid+1]:
                first_occurance_index=mid
                right=mid-1
            else:
                left=mid+1
        return first_occurance_index           

        
