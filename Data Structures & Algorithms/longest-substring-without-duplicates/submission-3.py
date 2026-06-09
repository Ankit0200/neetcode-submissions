class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        max_str=1
        loop_ran=False
        for char in s: 
            loop_ran=True

            if char in seen:
                if max_str<len(seen):
                    max_str=len(seen)
                    seen=set()
                    seen.add(char)
            else:
                    seen.add(char)
        if not loop_ran:
            max_str=0
        return max_str
            
            

