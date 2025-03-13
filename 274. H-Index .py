class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        papers_count = [0]*(n+1)

        for c in citations : 
            papers_count[min(c,n)] +=1
        
        h = n
        papers = papers_count[h]

        while papers < h : 
            h-=1
            papers += papers_count[h]
        
        return h


    #Time O(n)