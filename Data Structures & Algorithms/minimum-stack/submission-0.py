class MinStack:

    def __init__(self):
        self.my_arr=[]
        
        

    def push(self, val: int) -> None:
        self.my_arr.append(val)
        

    def pop(self) -> None:
        self.my_arr.pop()
        

    def top(self) -> int:
        return self.my_arr[-1]
        

    def getMin(self) -> int:
        return min(self.my_arr)
