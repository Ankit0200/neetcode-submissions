class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_val=None
        my_stack=[]
        for char in tokens:
            if char not in "+-/*":
                my_stack.append(char)
            else:
                b=int(my_stack.pop())
                a=int(my_stack.pop())

                if char == "+":
                    my_stack.append(b+a)
                elif char =="-":
                    my_stack.append(a-b)
                elif char =="*":
                    my_stack.append(b*a)
                elif char =="/":
                    print(a)
                    my_stack.append(int(a/b))
                
        return int(my_stack[-1])


          

        

        
        