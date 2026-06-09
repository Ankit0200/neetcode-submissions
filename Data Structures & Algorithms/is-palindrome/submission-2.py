class Solution:
    def isPalindrome(self, s: str) -> bool:
        org_length=len(s)
        i=0
        j=len(s)-1
      
        s=s.lower()

        while i!=j:
            print("**",{i})
           
           
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                print("wasn;t")
                j-=1
            elif s[i]==s[j]:
                i+=1
                j-=1
            elif s[i]!=s[j]:
                return False
        return True
            
           







        # s=s.strip()
        # s=s.lower()
        # reverse=''
        
        # # print(length)
        # original=''

        # for char in s:
        #     if char.isalnum():
        #         s.remove(cahr)
        # length=-len(original)

        # for i in range(-1,length-1,-1):
        #     if original[i].isalnum():
        #         reverse+=original[i]
            
        # print(reverse)
        # if reverse==original:
        #     return True
        # else:
        #     return False
            



        