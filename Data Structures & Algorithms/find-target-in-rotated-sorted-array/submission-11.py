class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low=0
        high=len(nums)-1
        res=9999999999999
        indexx=None
        
        while low<=high:
           guess=(low+high)//2

           if nums[guess]> nums[high]:
                low=guess+1
           else:
                
                if nums[guess]<res:
                    res=nums[guess]
                    indexx=guess
                high=guess-1
        if target == nums[indexx]:
            return indexx       

        elif target > nums[indexx] and target <= nums[-1]:
            
            low=indexx
            high=len(nums)-1
        elif target > nums[indexx] and target >= nums[0]:
           
            low=0
            high=indexx
        
        while low<=high:
            mp=(low+high)//2
            
            if nums[mp]<target:
                low=mp+1
            elif nums[mp]>target:
                high=mp-1
            elif target == nums[mp]:
                return mp
        
    
        

        
        return -1
            
        
        

    


           
            

            
        
           
        


        