class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        for num in nums :
            if num in dict :
                dict[num] += 1
            else :
                dict[num] = 1
        
        max_count = -1 
        ans = -1 
        for key , val in dict.items():
            if val > max_count :
                max_count = val
                ans = key
        
        return ans

        # Time : O(n)
        # Space : O(n)

        