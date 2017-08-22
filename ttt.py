# Tic Tac Toe player
#
# Uses full-depth search to find best move.
# Otherwise, not very creative.
#
# Jon Leete - August 2017

import random


########## Set up initial configuration ##########

# The board: just a string of X's, O's and spaces (intially all spaces)
board = ' ' * 9
# The players. X = human, O = computer
players = ['X', 'O']
# State variable
playing = True

# Set first player.
player = random.randint(0, 1)

########## Define functions ##########

# Print the board to the console.
#
def showBoard(board):
	print('\n---+---+---\n'.join(rows(board)))
def rows(board):
	r = []
	for i in range(3):
		start = i * 3
		r.append(' ' + ' | '.join(board[start:start+3]) + ' ')
	return r

# Does the specified player win?
#
def wins(board, players, player):
	c = players[player]
	return horizontalWin(board, c) or verticalWin(board, c) or diagonalWin(board, c)
def horizontalWin(board, c):
	for row in range(3):
		won = True
		for col in range(3):
			if board[row * 3 + col] != c:
				won = False
		if won:
			return True
	return False
def verticalWin(board, c):
	for col in range(3):
		won = True
		for row in range(3):
			if board[row * 3 + col] != c:
				won = False
		if won:
			return True
	return False
def diagonalWin(board, c):
	return (board[0] == c and board[4] == c and board[8] == c) or (board[2] == c and board[4] == c and board[6] == c)


# Make a move on the specified board, return a new board with the move made.
#
def makeMove(board, players, player, move):
	return board[:move] + players[player] + board[(move+1):]

# Find a move for the current player.
# If the current player is human, ask her/ if computer, calculate.
#
def getMove(board, players, player):
	if players[player] == 'X':
		move = int(input('Enter square to move (1-9): ')) - 1
	else:
		move = findBestMove(board, players, player)
	return move

# Find the best move for the current player.
#
def findBestMove(board, players, player):
	possibleMoves = available(board)
	bestMove = None
	maxScore = -1000
	for move in possibleMoves:
		tempBoard = makeMove(board, players, player, move)
		thisMoveScore = score(tempBoard, players, player)
		if thisMoveScore > maxScore:
			bestMove = move
			maxScore = thisMoveScore
	if bestMove == None:
		bestMove = possibleMoves[0]
	return bestMove

# Score the board for the current player.
#
def score(board, players, player):
	if wins(board, players, player):
		return 1
	elif full(board):
		return 0
	else:
		opponent = 1 - player
		opponentMove = findBestMove(board, players, opponent)
		tempBoard = makeMove(board, players, opponent, opponentMove)
		return -score(tempBoard, players, opponent)

# Is the board full?
#
def full(board):
	return not ' ' in board

# Return a list of open positions on the board.
#
def available(board):
	moves = []
	for i in range(len(board)):
		if board[i] == ' ':
			moves.append(i)
	return moves

########## Actually play the game ##########

while playing:
	print 'It is player ' + players[player] + '\'s turn.'
	move = getMove(board, players, player)
	print 'Player ' + players[player] + ' picked ' + str(move) + '\n'
	board = makeMove(board, players, player, move)
	showBoard(board)

	playing = not wins(board, players, player) and not full(board)
	if playing:
		player = 1 - player

if wins(board, players, player):
	print('Player ' + players[player] + ' wins!')
else:
	print('The game is a tie.')

