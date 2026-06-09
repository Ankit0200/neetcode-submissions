class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l_p=0
        r_p=len(heights)-1
        max_val=0

        while True:
            val=(r_p-l_p)*min(heights[r_p],heights[l_p])

            if val>=max_val:
                max_val=val
            if heights[l_p]<heights[r_p]:
                l_p+=1
            elif heights[l_p]>heights[r_p]:
                r_p-=1
            else:
                return max_val
        

