class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window=len(s1)
        
        l=0
        r=window-1
        count=defaultdict(int)
        standard=defaultdict(int)
    
        for i in range(window):
            
            standard[s1[i]]+=1
      
        for i in range(window):
            count[s2[i]]+=1
        
        
        while r<len(s2):
            if count == standard:
                return True
            else:
               
                count[s2[l]]-=1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                
                r+=1
                l+=1
              
                if r ==len(s2):
                    return False

                count[s2[r]]+=1
        return False

            
        

            







            


        