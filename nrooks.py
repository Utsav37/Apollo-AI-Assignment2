#!/usr/bin/env python3
# nrooks.py : Solve the N-Rooks problem!
# D. Crandall, 2016
# Updated by Zehua Zhang, 2017 ---- Updated by Utsav Patel

# run following commands if program does not run
# dos2unix nrooks.py
# chmod u+x nrooks.py
# python nrooks.py 5    or ./nrooks.py 5

# The N-rooks problem is: Given an empty NxN chessboard, place N rooks on the board so that no rooks
# can take any other, i.e. such that no two rooks share the same row or column.

import sys
# import time
# start_time = time.time()
flag =1

# Count # of pieces in given row
def count_on_row(board, row):
    return sum( board[row] ) 

# Count # of pieces in given column
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] ) 

# Count total # of pieces on board
def count_pieces(board):
#    print("sum([ sum(row) for row in board ] ) is :",sum([ sum(row) for row in board ] ))
    return sum([ sum(row) for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ " ".join([ "R" if col else "_" for col in row ]) for row in board])

# Add a piece to the board at the given position, and return a new board (doesn't change original)
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Get list of successors of given board state
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

def successors2(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) if((board[r][c]!=1) and (sum( board[r] )==0 ) and (sum( [ row[c] for row in board ] )==0))]

# Here we have solved two problems: not allowing N+1 rooks and not allowing move that generates same board ie not adding a rook at all
def successors3(board):
    global flag
    l=[]
    for c in range(0,N):
        for r in range(0,N):
            if((board[r][c]!=1) and (count_on_row(board, r) == 0) and (count_on_col(board, c) ==0)):
                if(sum( [ row[c-1] for row in board ] )==1 or flag<=N):
                    l.append(add_piece(board, r, c))
                    flag=flag+1
    return l


# check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N

# def is_goal(board):
#     return count_pieces(board) == N and \
#         all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
#         all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )


# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        for s in successors3( fringe.pop() ):
            if is_goal(s):
                return(s)
            fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
N = int(sys.argv[1])
#N=3
initial_board = [[0]*N]*N
#print("initial board is : ",initial_board)
#print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve(initial_board)
#print("solution is : ",solution)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")

# print("--- {} seconds ---".format(time.time() - start_time))

