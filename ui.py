
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
