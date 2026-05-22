class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals=[]
        current_start,current_end=intervals[0]
        for interval_start,interval_end in intervals[1:]:
            if current_end < interval_start:
                merged_intervals.append([current_start,current_end])
                current_start,current_end=interval_start,interval_end
            else:
                current_end = max(current_end, interval_end)    
        merged_intervals.append([current_start,current_end])
        return merged_intervals    

        
