class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        total_length=len(s)
        dash_count=s.count("-")
        char_count=total_length-dash_count
        first_group_size=char_count%k
        if first_group_size==0:
            first_group_size=k
        result=[]
        current_group_count=first_group_size
        for index,character in enumerate(s):
            if character=="-":
                continue
            result.append(character.upper()) 
            current_group_count-=1
            if current_group_count==0:
                current_group_count=k
                if index!=total_length-1:
                    result.append("-")  
        return "".join(result).rstrip("-")           
              


