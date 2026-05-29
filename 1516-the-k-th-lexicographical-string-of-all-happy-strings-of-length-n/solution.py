class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(current_string:List[str],result_list:List[str])->None:
            if len(current_string)==n:
                result_list.append("".join(current_string))
                return
            if  len(result_list)>=k:
                return
            for char in "abc":
                if not current_string or current_string[-1]!=char:
                    current_string.append(char)
                    backtrack(current_string,result_list)
                    current_string.pop()
        all_happy_strings=[]
        current_build=[]
        backtrack(current_build,all_happy_strings)
        return "" if len(all_happy_strings)<k else all_happy_strings[k-1]              
        
