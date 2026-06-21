class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # m = len(matrix) (You actually don't need this variable anymore!)
        n = len(matrix[0]) - 1

        for row in matrix:
            if row[0] > target:
                return False
            
            # FIX 1: Removed the len(matrix) < 2 logic. 
            # If the last number is too small, just move to the next row!
            if row[n] < target:
                continue
                
            elif row[n] == target:
                return True
                
            elif row[n] > target:
                l = 0
                r = n
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] < target:
                        l = mid + 1
                    elif row[mid] > target:
                        r = mid - 1
                    elif row[mid] == target:
                        return True
                # If we binary searched the correct row and didn't find it, 
                # we can safely return False immediately.
                return False

        # FIX 2: The catch-all return. 
        # If the loop finishes checking every row and never finds the target, return False.
        return False