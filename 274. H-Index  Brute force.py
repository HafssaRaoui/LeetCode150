class Solution:
    def hIndex(self, citations: List[int]) -> int:

        h = 0 
        num_papers = 0
        h_valid = 0

        while(h == num_papers and h < len(citations)):
            h+=1
            num_papers =0
            for p in range(len(citations)):
                if citations[p] >= h :
                    num_papers +=1
                
                if (h == num_papers):
                    h_valid = h
                    break
        
        return h_valid
    

        #Time O(n²)
        #this Brute Force solution consists on checking the h_index from 0 until it's no more possible to increment