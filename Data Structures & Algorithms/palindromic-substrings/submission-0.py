class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.solve(s, 0) 
    

    def is_palindrome(self, s: str, start: int, end: int) -> int:
        status = True
        while start < end:
            if s[start] != s[end]:
                status = False 
                break
            start += 1 
            end -= 1 
        
        return status
        

    def solve(self, s: str, start: int) -> int:
        if start == len(s):
            return 0 

        count = 0
        for index in range(start, len(s)):
            if self.is_palindrome(s, start, index):
                count += 1 
            
        return count + self.solve(s, start + 1)
    
        
    


        