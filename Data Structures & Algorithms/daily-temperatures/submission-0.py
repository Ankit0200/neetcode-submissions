class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0] *len(temperatures)
        stack=[] # Its gonna be pair of index and temperature.
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res