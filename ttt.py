# Tic Tac Toe player
#
# Uses full-depth search to find best move.
# Otherwise, not very creative.
#
# Jon Leete - August 2017


from ui import *
from init import *
from play import *

########## Set up initial configuration ##########

# The board: just a string of X's, O's and spaces (intially all spaces)
board = newBoard()
# The players. X = human, O = computer
players = players()
# State variable
playing = True

# Set first player.
player = randomStartPlayer(players)

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

