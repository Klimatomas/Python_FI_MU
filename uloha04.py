__author__ = 'Tomas'


def strategy(state):
	pass


def is_valid(move):
	pass


def tictactoe(size, human_starts=True):
	field = size * ['_']
	print field
	while True:
		if human_starts:
			move = input("Insert your move: ")
			is_valid(move)
			for i in range(len(field)):
				if move == i + 1:
					print field[i]
					if field[i] == "X":
						print "invalid move"
					else:
						field[i] = "X"

		print field


tictactoe(9)
