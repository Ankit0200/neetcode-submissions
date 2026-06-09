class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        my_list=[]

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1
            while l<r:
                our_val=a+nums[l]+nums[r]

                if our_val<0:
                    l+=1
                elif our_val>0:
                    r-=1
                elif our_val==0:
                    my_list.append([a,nums[l],nums[r]])
                    l+=1
                    if nums[l]==nums[l-1] and l<r:
                        l+=1

        
        return my_list
            

        