class Solution:
    def maskPII(self, s: str) -> str:
        if s[0].isalpha():
            s=s.lower()
            at_position=s.find('@')
            return s[0]+'*****'+s[at_position-1:]   
        digits_only=''.join(char for char in s if char.isdigit())
        country_code_length=len(digits_only)-10 
        suffix="***-***-"+digits_only[-4:]
        if country_code_length==0:
            return suffix
        return f'+{"*"*country_code_length}-{suffix}' 

        
