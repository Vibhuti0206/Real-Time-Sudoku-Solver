# # # -*- coding: utf-8 -*-
# # """
# # Created on Thu Apr 29 22:19:05 2021

# # @author: va
# # """

class EntryData:
    def __init__(self, r, c, n):
        self.row = r
        self.col = c
        self.choices = n

    def set_data(self, r, c, n):
        self.row = r
        self.col = c
        self.choices = n
    

def solve_sudoku(matrix):
    cont = [True]
   
    for i in range(9):
        for j in range(9):
            if not can_be_correct(matrix, i, j): 
                return
    sudoku_helper(matrix, cont) 

def sudoku_helper(matrix, cont):
    if not cont[0]: 
        return

    best_candidate = EntryData(-1, -1, 100)
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0: 
                num_choices = count_choices(matrix, i, j)
                if best_candidate.choices > num_choices:
                    best_candidate.set_data(i, j, num_choices)

  
    if best_candidate.choices == 100: 
        cont[0] = False 
        return

    row = best_candidate.row
    col = best_candidate.col

   
    for j in range(1, 10):
        if not cont[0]: 
            return

        matrix[row][col] = j

        if can_be_correct(matrix, row, col):
            sudoku_helper(matrix, cont)

    if not cont[0]: 
        return
    matrix[row][col] = 0 

def count_choices(matrix, i, j):
    can_pick = [True,True,True,True,True,True,True,True,True,True]; 

    for k in range(9):
        can_pick[matrix[i][k]] = False

   
    for k in range(9):
        can_pick[matrix[k][j]] = False;

    
    r = i // 3
    c = j // 3
    for row in range(r*3, r*3+3):
        for col in range(c*3, c*3+3):
            can_pick[matrix[row][col]] = False

   
    count = 0
    for k in range(1, 10): 
        if can_pick[k]:
            count += 1

    return count
###################


def can_be_correct(matrix, row, col):

    # Check row
    for c in range(9):
        if matrix[row][col] != 0 and col != c and matrix[row][col] == matrix[row][c]:
            return False

    for r in range(9):
        if matrix[row][col] != 0 and row != r and matrix[row][col] == matrix[r][col]:
            return False

 
    r = row // 3
    c = col // 3
    for i in range(r*3, r*3+3):
        for j in range(c*3, c*3+3):
            if row != i and col != j and matrix[i][j] != 0 and matrix[i][j] == matrix[row][col]:
                return False

    return True

N= 9 
def all_board_non_zero(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j] == 0:
                return False
    return True

def isSafe(grid, row, col, num):
   
    global N
    for x in range(9):
        if grid[row][x] == num:
            return False
 
 
    for x in range(9):
        if grid[x][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSuduko(grid, row, col):
    global N
    if (row == N - 1 and col == N):
        return True
  
    if col == N:
        row += 1
        col = 0
 
    if grid[row][col] > 0:
        return solveSuduko(grid, row, col + 1)
    for num in range(1, N + 1, 1):
    
        if isSafe(grid, row, col, num):
         
            grid[row][col] = num
 
          
            if solveSuduko(grid, row, col + 1):
                return True
 
        grid[row][col] = 0
    return False