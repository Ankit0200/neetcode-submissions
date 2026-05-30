class Solution:
  

    def encode(self, strs: List[str]) -> str:
        my_str=''
        for char in strs:
            my_str=my_str + str(len(char))+"#"+char
    
        return my_str

        

    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i < len(s):
            j=i
            while(s[j]!="#"):
                j+=1
            my_length=int(s[i:j])
            res.append(s[j+1:j+1+my_length])
            i=j+1+my_length 
        return res

            

        
            