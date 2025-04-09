class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        n = len(haystack)
        m = len(needle)
        i = 0 
        while i < n :
            
            if haystack[i:i+m] == needle :
                return i

            else :
                i+=1
        
        return -1