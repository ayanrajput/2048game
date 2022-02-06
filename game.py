# -------------------------Initalizing the board----------------------

# dimension of board ex 4x4 8x8
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
                line+=" "*(spacesRequired-len(str(c)))+str(c)
        print(line)




    