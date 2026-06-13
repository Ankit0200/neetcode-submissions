class Solution:
    def isValid(self, s: str) -> bool:
        my_map={"}":"{",")":"(","]":"["}
        my_stack=[]
        if len(s)==0:
            return False
        for char in s:
            if char in "{([":
                my_stack.append(char)
            elif char in my_map:
                if len(my_stack)==0 or my_stack[-1]!=my_map[char]:
                    
                    return False
                else:
                    my_stack.pop()
        print(my_stack)
        return len(my_stack)==0
                
                

