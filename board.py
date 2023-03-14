class pbord:
    def __init__(self,pq,r,c,p):
        self.pq = pq # piece
        self.r = r #row
        self.c = c #column
        self.p = p # which player 1 is White, 2 is Black, # 0 is nothing
import numpy as np

board = []#for testing
boarstr = ""

def newBoard(board):
    board[0].pq="**Rk**w" # set pieces
    board[7].pq="**Rk**w"
    board[1].pq="**Kn**w"
    board[6].pq="**Kn**w"
    board[2].pq="**Bp**w"
    board[5].pq="**Bp**w"
    board[3].pq="**Qn**w"
    board[4].pq="**Kg**w"
    for t in range (8):
        board[t+8].pq="**Pn**w"
        board[t].p = 1 #set pieces to white
        board[t+8].p = 1
    board[56].pq="**Rk**b " # set pieces
    board[63].pq="**Rk**b "
    board[57].pq="**Kn**b "
    board[62].pq="**Kn**b "
    board[58].pq="**Bp**b "
    board[61].pq="**Bp**b "
    board[59].pq="**Qn**b "
    board[60].pq="**Kg**b "
    for t in range (8):
        board[t+48].pq="**Pn**b "
        board[t+48].p = 2 #set pieces to black
        board[t+56].p = 2
    return
def makeBoard(board):#makes empty board
    for x in range(8):
        for y in range (8):
            adb = pbord("         ",x,y,0)
            board.append(adb)
    return
#makeBoard(board)
#newBoard(board)

# if p=0, use 8 spaces

def printboardt(board): #for testing printing out board in terminal
    x=0
    for i  in board:
        print( "|" + i.pq , end = "")
        x+=1
        if x == 8:
            print("| %s" %(i.r+1))
            x=0
        bL = [" A "," B   "," C   "," D  "," E  "," F  "," G  "," H "]
    for i  in bL:
        print("|   " + i , end = "")

def printboard(board): #making string to print
    x=0
    boardstr=" "
    for i  in board:
        boardstr += "|" 
        boardstr += str(i.pq)
        x+=1
        if x == 8:
            boardstr += "| "
            boardstr += str(i.r+1)
            boardstr += "\n"
            x=0
        bL = [" A "," B   "," C   "," D  "," E  "," F  "," G  "," H "]
    z=0
    for i  in bL:
        boardstr +="|"
        boardstr += " "
        boardstr += i
        z+=1
        #if (z==1):
            #boardstr += " "
        #else:
        boardstr += "  "
    return boardstr

def let2num(let):
    let=let.upper()
    if (let=="A"):
        return 1
    elif (let=="B"):
        return 2
    elif (let=="C"):
        return 3
    elif (let=="D"):
        return 4
    elif (let=="E"):
        return 5
    elif (let=="F"):
        return 6
    elif (let=="G"):
        return 7
    elif (let=="H"):
        return 8
    else:
        return 0

def interpret(comm):
    mv = []
    for i in range(len(comm)):
        if (comm[i]!=" "):
            print(comm[i],end="")
            if(let2num(comm[i])!=0):
                z=let2num(comm[i])
                print(" l ",end="")
            else:
                z=int(comm[i])
                print(" i ",end="")
            print(z)
            mv.append(z)
    return mv


#p=printboard(board)
#print(p)
#mx = "E7B2"
#bx = interpret(mx)
#for i in bx:
#    print(i)
