class Solution:
    def magicalString(self, n: int) -> int:
        if n==0:
            return 0
        magical_string=[1,2,2]
        group_count_index=2
        while len(magical_string)<n:
            prev=magical_string[-1]
            current=3-prev
            repeat=magical_string[group_count_index]  
            magical_string.extend([current]*repeat)
            group_count_index+=1
        return magical_string[:n].count(1)    

        
