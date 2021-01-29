'''
Boggle is a game played on a 4 x 4 grid of letters. 

The goal is to find as many words as possible that can be formed by a sequence
of adjacent letters in the grid, using each cell at most once. 

Given a game board and a dictionary of valid words, implement a Boggle solver.
'''


solutions = set()
visitedPairs = set()
#words - a dictionary of words
#board - a 2D array with letters
#curWord - string of the word we have build up so far through traversal
# i, j - ints, coordinates we use to index into each cell in the boggle board
def solveBoggle(words, board, curWord, i, j):
    if (i>3) or (j>3) or (i<0) or (j<0):
        return
    if (i,j) in visitedPairs:
        return
    visitedPairs.add((i,j))
    if curWord in words:
        solutions.add(curWord)
    curWord += board[i][j]
    solveBoggle(words,board, curWord, i, j+1)
    solveBoggle(words,board, curWord, i+1, j)
    solveBoggle(words,board, curWord, i+1, j+1)
    solveBoggle(words,board, curWord, i-1, j)
    solveBoggle(words,board, curWord, i-1, j-1)
    solveBoggle(words,board, curWord, i, j-1)
    