class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
      
      
        
        indexrow=0

        for row in board:
            freq=[[] for _ in range(10)]
           
            
            for char in row:
                if char!='.':
                    char=int(char)
                    if len(freq[char])==0:
                        freq[char].append(char)
                        
                    else:
                        
                        return False
        
        i=0
        j=0

        while i<9:
            column=[[] for _ in range(10)]
            j=0
            while j<9:
                
                if board[j][i]!='.':

                    char=int(board[j][i])
                    # print(char)
                    
                    if len(column[char])==0:
                        column[char].append(char)
                    else:
                        # print(column)
                        return False
                j+=1
            i+=1
        
        # my_matrix[3][3]

        for square in range(9):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = (square//3) * 3 + i
                        col = (square % 3) * 3 + j
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])
                return True





        



        





        
            
            
      
    
       
            
            
            

        