class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_val=None
        my_stack=[]
        for char in tokens:
            if char not in "*-+/":
                print("woo")
                my_stack.append(char)
                my_val=int(my_stack[0])
            else:
                print("came here")
                my_val = eval(f"{int(my_stack[-2])} {char} {int(my_stack[-1])}")
                del my_stack[-1]
                del my_stack[-1]
                print(my_stack)
                print(my_val)
                my_stack.append(my_val)
    
        return int(my_val)

        

        
        