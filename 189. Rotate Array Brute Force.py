class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        res=[0]*len(nums)
        for i in range(len(nums)):
            pos = (i+k)%len(nums)
            res[pos] = nums[i]
        
        nums[:]= res

        # time complexity O(n)
        # space complexity O(n)