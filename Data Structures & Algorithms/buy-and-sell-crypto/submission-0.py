class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff=0
        nums=prices
        for i in range(len(prices)):
            if i>0:
                min_pos=min(nums[:i])
            else: 
                min_pos=nums[0]
            if min_pos<nums[i]:
                pass

            else:
                if i==len(prices)-1:
                    max_pos=nums[-1]
                else:
                
                    max_pos=max(nums[i+1:])
                    print(max_pos)
                    if max_pos > diff and max_pos>nums[i]: 
                        print(diff)
                        diff=max_pos-nums[i]
                        print(diff)
                        
        return diff
                
        



        
        