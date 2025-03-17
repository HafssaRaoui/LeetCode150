class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l_mult = 1
        r_mult = 1
        left =[0]*n
        right =[0]*n


        for i in range(n) :
            j = -i-1

            left[i] = l_mult
            right[j] = r_mult

            l_mult *= nums[i]
            r_mult *= nums[j]

        
        return [l*r for l,r in zip(left,right)]
