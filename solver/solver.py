def print_sudoku(sudoku):
  print('\n\n')
  for i in range(len(sudoku)):
    line = ""
    if i == 3 or i == 6:
      print("---------------------")
    for j in range(len(sudoku[i])):
      if j== 3 or j == 6:
        line+='| '
      line += str(sudoku[i][j])+" "
    print(line)
  print("\n\n")
def find_next_cell_to_fill(sudoku):
  for x  in range(9):
    for y in range(9):
      if sudoku[x][y] == 0:
        return x , y
  return -1 , -1 

def is_valid(sudoku , i , j , e):
  row_ok = all([e != sudoku[i][x] for x in range(9)])
  if row_ok:
    column_ok = all([e != sudoku[x][j] for  x in range(9)])
    if column_ok:
      sec_topX , sec_topY = 3*(i//3) , 3*(j//3)
      for x  in range(sec_topX , sec_topX+3):
        for y in range(sec_topY , sec_topY+3):
          if sudoku[x][y] == e:
            return False
      return True
  return False

def solve_mat(sudoku , i =0 ,j =0):
  i , j = find_next_cell_to_fill(sudoku)
  if i == -1:
    return True
  for e in range (1, 10):
    if is_valid(sudoku , i ,j ,e):
      sudoku[i][j] = e
      if solve_mat(sudoku , i, j):
        return True
      sudoku[i][j] = 0
  return  False