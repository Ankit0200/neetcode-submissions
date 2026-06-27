class Solution:
    def findMin(self, nums: List[int]) -> int:

        low=0
        high=len(nums)-1
        res=99999999999

        while low<=high:
            guess=(low+high)//2
            if nums[guess]>nums[high]:
                low=guess+1
            elif nums[guess]<=nums[high]:
                res=min(res,nums[guess])
                high=guess-1

            
        return res
            




                
            








        