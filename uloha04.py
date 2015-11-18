__author__ = 'Tomas'


def strategy(state):
	print "som tu"
	for i in range(len(state)):
		if state[i] == "X" == state[i + 1]:
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
	x = False
	# podminka pro zacinani pocitacem/hracem ... je to trochu dementni
	if human_starts:
		turn = 0
	else:
		turn = 1
	while not x:
		if turn % 2 == 0:
			turn += 1
			move = input("Insert your move: ")
			valid = is_valid(move - 1, field)
			while not valid:
				field[move - 1] = "X"
		else:
			turn += 1
			strategy(field)

		print " ".join(field)
		print ""
		x = victory_condition(field)


tictactoe(10, False)
