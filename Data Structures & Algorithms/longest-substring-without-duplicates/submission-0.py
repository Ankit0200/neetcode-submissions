class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        max_str=0
        for char in s: 
            if char in seen:
                if max_str<len(seen):
                    max_str=len(seen)
                    seen=set()
                    seen.add(char)
            else:
                    seen.add(char)
        return max_str
            
            

