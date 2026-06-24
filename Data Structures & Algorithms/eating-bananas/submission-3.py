class Solution:


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        my_dict=defaultdict(int)
        max_m=max(piles)

        l=1
        
        r=max_m
        my_bucket=[]
        m=(l+r)//2
        

        while l<=r:
            val=0
           

            for char in piles:
                if m!=0:
                   
            
                    if (char % m) ==0:
                        val+=int(char//m)
                    else:
                        val+= (char//m)+  1
            
            if val<=h:
                print("camer here")
                my_bucket.append(m)
                r=m-1
            elif val>h:
                l=m+1
            m=(l+r)//2
        
        return min(my_bucket)
                
                
                



        
  




        
        
        


        