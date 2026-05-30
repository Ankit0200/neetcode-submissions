class Solution:
    def maxArea(self, heights: List[int]) -> int:
        base=0
        p_l=base+1

        max_water=0

        for i,a in enumerate(heights):
            p_l=i+1
        
            while (p_l) <len(heights):
                
                val=(p_l-i)*min(heights[i],heights[p_l])

                if val >=max_water:
                    max_water=val
                p_l+=1
            
        return max_water


