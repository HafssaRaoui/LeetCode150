class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min = len(strs[0])
        n = len(strs)
        for i in range(1,n):
            if len(strs[i]) < min : 
                min = len(strs[i])
        
        k = 0
        while k < min : 
            for s in strs :
                if s[k] != strs[0][k]:
                    return s[:k]
            
            k+=1
        
        return strs[0][:k]
    


        #Time O(n*m) 