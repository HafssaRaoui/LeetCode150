class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        n = len(s)
        str = ''
        for k in range(n):
            ch = s[k].lower()
            if ('a' <= ch <= "z" or '0' <=ch <= '9'):
                str += ch
   
        i,j= 0, len(str)-1
        while i < j :
            
            if str[i] != str[j]:
                return False
            i+=1
            j-=1
        
        return True
        