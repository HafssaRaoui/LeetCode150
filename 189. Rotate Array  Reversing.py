class Solution :
        


        def rev(self,nums: List[int], l : int , r : int) -> None:
                while l < r :
                        nums[l],nums[r] = nums[r],nums[l]
                        l,r = l+1 , r-1
        
        def rotate(self, nums: List[int], k: int) -> None:
                
                k = k % len(nums)
                self.rev(nums,0,len(nums)-1)
                self.rev(nums,0,k-1)
                self.rev(nums,k,len(nums)-1)
                
                                
