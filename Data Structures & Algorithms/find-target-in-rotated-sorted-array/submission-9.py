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
                    print("Came jere")
                    res=nums[guess]
                    indexx=guess
                high=guess-1
                

        low=0
        high=indexx
        print(indexx)
        
        while low<=high:
            mp=(low+high)//2
            
            if nums[mp]<target:
                low=mp+1
            elif nums[mp]>target:
                high=mp-1
            elif target == nums[mp]:
                return mp
        
        low=indexx
        high=len(nums)-1
        while low<=high:
            mp=(low+high)//2
            if nums[mp]<target:
                low=mp+1
            elif nums[mp]>target:
                high=mp-1
            elif target == nums[mp]:
                return mp
        

        
        return -1
            
        
        

    


           
            

            
        
           
        


        