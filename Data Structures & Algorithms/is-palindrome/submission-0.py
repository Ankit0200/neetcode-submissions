class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        s=s.lower()
        reverse=''
        
        # print(length)
        original=''

        for char in s:
            if char.isalnum():
                original+=char
        length=-len(original)

        for i in range(-1,length-1,-1):
            if original[i].isalnum():
                reverse+=original[i]
            
        print(reverse)
        if reverse==original:
            return True
        else:
            return False
            



        