class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l=0
        r=k-1
        max_list=[]
        s=nums
        

        while r<len(nums):
            if l==0:
                maxm=max(s[l:r+1])
            else:
                maxm=max(s[l:r+1])

          
            
            max_list.append(maxm)
            l+=1
            r+=1

        return max_list


            
