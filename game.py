import random
import copy
# -------------------------Initalizing the board----------------------

# dimension of board ex 4x4 8x8
dimension=4

# winning number 
winning_number=2048

# board
board=[[0 for i in range(dimension)]for j in range(dimension)]

# ------------------------ Helper functions  ------------------------

# get a random value to fill from (2,4)
def getNewRandomValue():
    rand=random.randint(1,8)
    if rand==1:
        return 4
    else:
        return 2

# filling random places
def fillRandomEmptyPlace(currBoard,val):
    while True:
        r_num=random.randint(0,dimension-1)
        c_num=random.randint(0,dimension-1)
        if currBoard[r_num][c_num]==0:
            currBoard[r_num][c_num]=val
            break
    return currBoard

# filling two random values in the board
for _ in range(2):
    val=getNewRandomValue()
    fillRandomEmptyPlace(board,val)

# -------------------- Printing the board  ---------------------------

def displayBoard():
    # maximum value in the board
    max_val=0
    for r in board:
        for c in r:
            if c>max_val:
                max_val=c

    # spaces required
    spacesRequired=len(str(max_val))

    # now printing the board
    for r in board:
        line="|"
        for c in r:
            if c==0:
                line+=" "*spacesRequired+"|"
            else:
                line+=" "*(spacesRequired-len(str(c)))+str(c)+"|"
        print(line)

# -----------------  Merging Functions   -------------------

# merging single row to left
def mergeRowLeft(r):
    # moving everything left first time
    for i in range(dimension-1):
        for j in range(dimension-1,0,-1):
            if r[j-1]==0:
                r[j],r[j-1]=r[j-1],r[j]
    # merging
    for i in range(dimension-1):
        if r[i]==r[i+1]:
            r[i]*=2
            r[i+1]=0
    # moving everything left second time
    for j in range(dimension-1,0,-1):
        if r[j-1]==0:
            r[j],r[j-1]=r[j-1],r[j]
    return r

# mergering board left
def mergeBoardLeft(currBoard):
    for i, r in enumerate(currBoard):
        currBoard[i]=mergeRowLeft(r)
    return currBoard

# merging board right
def mergeBoardRight(currBoard):
    for i, r in enumerate(currBoard):
        r.reverse()
        r=mergeRowLeft(r)
        r.reverse()
        currBoard[i]=r
    return currBoard

# transpose function
def transpose(currBoard):
    for i in range(dimension):
        for j in range(i,dimension):
            currBoard[i][j],currBoard[j][i]=currBoard[j][i],currBoard[i][j]
    return currBoard

# merging board upwards
def mergeBoardUp(currBoard):
    currBoard=transpose(currBoard)
    currBoard=mergeBoardLeft(currBoard)
    currBoard=transpose(currBoard)
    return currBoard

# merging board downwards
def mergeBoardDown(currBoard):
    currBoard=transpose(currBoard)
    currBoard=mergeBoardRight(currBoard)
    currBoard=transpose(currBoard)
    return currBoard

# ---------------------- Staring the game and checking win or lose  -------------------

# function to check if player won
def ifPlayerWon(currBoard):
    for r in currBoard:
        for c in r:
            if c==winning_number:
                return True
    return False

# function to check if player lost
def ifPlayerLost(currBoard):
    tmp_board_lose=copy.deepcopy(currBoard)
    # testing all direction
    tmp_board_lose=mergeBoardLeft(tmp_board_lose)
    if tmp_board_lose==currBoard:
        tmp_board_lose=mergeBoardRight(tmp_board_lose)
        if tmp_board_lose==currBoard:
            tmp_board_lose=mergeBoardUp(tmp_board_lose)
            if tmp_board_lose==currBoard:
                tmp_board_lose=mergeBoardDown(tmp_board_lose)
                if tmp_board_lose==currBoard:
                    return True
    return False




print("Welcome to the "+str(winning_number)+" game.")
print("Win the game by getting the numeber "+str(winning_number) +" on the board")
print("Use 1 to merge left, 2 to merge right, 3 to merge top and 4 to merge down")
print("Here is the initial board")
displayBoard()    

continueGame=True

while continueGame:
    direction=input("Which direction to merge?")
    if direction not in {"1","2","3","4"}:
        print("Invalid Move")
        continue
    
    # temp board to check if anything changed in the board
    tmp_board=copy.deepcopy(board)

    if direction=="1":
        board=mergeBoardLeft(board)
    elif direction=="2":
        board=mergeBoardRight(board)
    elif direction=="3":
        board=mergeBoardUp(board)
    elif direction=="4":
        board=mergeBoardDown(board)

    # checking if nothing changed
    if board==tmp_board:
        print("Try a different move")
    else:
        if ifPlayerWon(board):
            print("Hurray!!! You won ")
            input()
            continueGame=False
        else:
            fillRandomEmptyPlace(board,getNewRandomValue())
            displayBoard()
            if ifPlayerLost(board):
                print("No more possible moves, you lose")
                input()
                continueGame=False



