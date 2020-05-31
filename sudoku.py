import numpy as np
import random 

board = np.array([[0,0,0,2,6,0,7,0,1],
                 [6,8,0,0,7,0,0,9,0],
                 [1,9,0,0,0,4,5,0,0],
                 [8,2,0,1,0,0,0,4,0],
                 [0,0,4,6,0,2,9,0,0],
                 [0,5,0,0,0,3,0,2,8],
                 [0,0,9,3,0,0,0,7,4],
                 [0,4,0,0,5,0,0,3,6],
                 [7,0,3,0,1,8,0,0,0]])


def find_missing(bd):
    for i in range(9):
        for j in range(9):
            if bd[i,j] == 0:
                return (i,j)
    return None


def is_valid(bd, num, coor):
    
    # Check row is valid
    for j in range(9):
        if bd[coor[0],j] == num:
            return False
    
    #Check column is valid
    for i in range(9):
        if bd[i, coor[1]] == num :
            return False
    
    # Check within block: 9 blocks in soduku
    
    block_i = coor[0] // 3
    block_j = coor[1] // 3
    
    for i in range(block_i*3, block_i*3 +3 ):
        for j in range(block_j*3, block_j*3 +3):
            if bd[i,j] == num and (i,j) != coor:
                return False
    return True


def solver(bd):
  """Solves Sudoku puzzle. Assumes missing values in Numpy Array matrix is coded as 0"""

    to_solve = find_missing(bd)
    
    if to_solve == None:
        return True
    else:
        for number in range(1,10):
            if is_valid(bd, number, to_solve):
                bd[to_solve] = number
                
                if solver(bd):
                    return True
                bd[to_solve] = 0
                
        return False
        
    
def gen_board():
    """Returns a tuple of randomly generated Sudoku and solution"""

    new_bd = np.zeros(81).reshape(9,9).astype('int64')
    new_bd[0,0] = random.randint(1,9)
    new_bd[1,3] = random.randint(1,9)
    
    if random.randint(0,1):
        if new_bd[0,0] + new_bd[1,3] > 9:
            new_num = abs(new_bd[0,0] - new_bd[1,3])
            while new_num == new_bd[0,0] or new_num == new_bd[1,3] or new_num ==0:
                new_num += 1
            new_bd[1,0] = new_num
        else:
            new_bd[1,0] = new_bd[0,0] + new_bd[1,3]  
           
    new_bd[2,6]= random.randint(1,9)
    new_bd[3,1]= random.randint(1,9)
    new_bd[4,4]= random.randint(1,9)
    new_bd[5,7]= random.randint(1,9)
    
    if random.randint(0,1):
        if new_bd[4,4] + new_bd[5,7]  > 9:
             new_num = abs(new_bd[4,4] - new_bd[5,7])
             while new_num == new_bd[4,4] or new_num == new_bd[5,7] or new_num ==0:
                 new_num += 1
             new_bd[5,4] = new_num
        else:
            new_bd[5,4] = new_bd[4,4] + new_bd[5,7]
            
    new_bd[2,6]= random.randint(1,9)
    new_bd[6,2]= random.randint(1,9)
    new_bd[7,5]= random.randint(1,9)
    
    if random.randint(0,1):
        if new_bd[6,2] + new_bd[7,5]> 9:
            new_num = abs(new_bd[6,2] - new_bd[7,5])
            while new_num == new_bd[6,2] or new_num == new_bd[7,5] or new_num ==0:
                new_num += 1
            new_bd[7,2] = new_num
        else:
            new_bd[7,2] = new_bd[6,2] + new_bd[7,5]
        
    new_bd[8,8]= random.randint(1,9)
    
    solver(new_bd)
    solution = new_bd.copy()
    
    n = random.randint(40,60)
    
    while n != 0:
        i = random.randint(0,8)
        j = random.randint(0,8)
        
        if new_bd[i,j] != 0:
            
            new_bd[i,j] = 0
            n -= 1
    
    
    return new_bd, solution
