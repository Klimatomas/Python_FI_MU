__author__ = 'Tomas'


def strategy(state):
	pass


def is_valid(move, field):
	for i in range(len(field)):
		if move <= len(field) and field[move] != "X":
			return True
		else:
			print "Not a valid move!"
			return False


def victory_condition(field):
	for i in range(len(field)):
		if field[i] == "X" == field[i + 1] == field[i + 2]:
			return True
		# WTF???!!!


def tictactoe(size, human_starts=True):
	field = size * ['_']
	x = victory_condition(field)
	while not x:
		if human_starts:
			move = input("Insert your move: ")
			is_valid(move - 1, field)
			if is_valid:
				field[move - 1] = "X"

		print " ".join(field)
		x = victory_condition(field)


tictactoe(10)
