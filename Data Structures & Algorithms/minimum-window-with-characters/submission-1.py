class Solution:
    def minWindow(self, s: str, t: str) -> str:
        standard=defaultdict(int)
        count=defaultdict(int)
        for char in range(len(t)):
            standard[t[char]]+=1

        have,need=0,len(standard)
        my_indexes=[-1,-1]
        my_length=999999999
        l=0

        for r in range(len(s)):
            my_char=s[r]

            count[my_char]+=1

            if my_char in standard and count[my_char]==standard[my_char]:
                have+=1
            
            while have == need:
                if my_length>(r-l+1):

                    my_indexes=[l,r+1]
                    my_length=r-l+1

                count[s[l]]-=1
               

                if s[l] in standard and count[s[l]]<standard[s[l]]:
                    have-=1
                l+=1
                
                
        
        if my_length>-1:
            return s[my_indexes[0]:my_indexes[1]]
        else:
            return ""
                

                

            





            

