class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map={}
        for current_index,value in enumerate(nums):
            if value in index_map and current_index-index_map[value]<=k:
                return True
            index_map[value]=current_index          
        return False    
