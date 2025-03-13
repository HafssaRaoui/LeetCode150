class Solution:
    def jump(self, nums: List[int]) -> int:
        n =len(nums)
        smallest = 0
        far , end = 0 ,0

        for i in range(n-1):
            far = max(far, i+nums[i])

            if i == end :
                smallest+=1
                end = far
        
        return smallest