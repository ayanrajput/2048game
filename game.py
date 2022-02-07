# -------------------------Initalizing the board----------------------

# dimension of board ex 4x4 8x8
import enum


dimension=4

# winning number 
winning_number=2048

# board
board=[[0 for i in range(dimension)]for j in range(dimension)]

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
    for i , r in enumerate(currBoard):
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




    