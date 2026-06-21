class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            middle_man=(l+r)//2
            print(middle_man)
            if nums[middle_man]>target:
                r=middle_man-1
            elif nums[middle_man]<target:
                l=middle_man+1
            else:
                return middle_man
        
        return -1

        
        