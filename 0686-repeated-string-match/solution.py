class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a,len_b=len(a),len(b)
        min_repeations=ceil(len_b/len_a)
        repeated_string_list=[a]*min_repeations
        for _ in range(3):
            repeated_string=''.join(repeated_string_list)
            if b in repeated_string:
                return min_repeations
            min_repeations+=1
            repeated_string_list.append(a) 
        return -1       

        
