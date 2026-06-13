class Solution:
    def isValid(self, s: str) -> bool:
        my_arr=[]
        for char in s:
            if char =="(" or char =="{" or char =="[":
                my_arr.append(char)
            if char =="}" or char =="]" or char ==")":
                if char =="}":
                    compare="{"
                elif char ==")":
                    compare="("
                elif char=="]":
                    compare="["

                if len(my_arr)<1:
                    return False
              
                if my_arr[-1]!=compare:
                    return False
                else:
                    my_arr.pop()
        if len(my_arr)==0:
            return True
        else:
            return False

        