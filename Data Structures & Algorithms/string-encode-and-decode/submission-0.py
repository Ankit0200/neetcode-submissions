class Solution:
  

    def encode(self, strs: List[str]) -> str:
        my_str=''
        for char in strs:
            my_str=my_str + char + "##"
    
        return my_str

        

    def decode(self, s: str) -> List[str]:
        listing=[item.strip() for item in s.split("##") ]
        return listing[:-1]
