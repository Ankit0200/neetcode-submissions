class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L_P=0
        R_P=1
        nums=prices
        max_profit=0
        
        while R_P <len(prices):

            if nums[R_P]>nums[L_P]:
                if max_profit<= (nums[R_P]-nums[L_P]):
                    max_profit=nums[R_P]-nums[L_P]
                R_P+=1
            
            else: 
                L_P+=1
                R_P+=1
        return max_profit
        
         
        
        

            
        