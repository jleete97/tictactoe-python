import random

# Create a new Tic Tac Toe "board"
def newBoard():
    return ' ' * 9

# Set up Tic Tac Toe players
def players():
    return ['X', 'O']

# Pick a random starting player
def randomStartPlayer(players):
    return random.randint(0, len(players)) - 1