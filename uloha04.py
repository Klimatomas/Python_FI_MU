from random import randint

__author__ = 'Tomas'


def strategy(state):
	# len(state)-2 je kvuli tomu aby pri kontrole nebyl index out of range
	for i in range(len(state) - 2):
		move = randint(1,len(state)-1)
		if state[i] == "X":

			# kontrola stavu [ X X _ ]
			if state[i + 1] == "X":
				move = i + 2
				break

			# kontrola stavu [ X _ X ]
			elif state[i + 2] == "X":
				move = i + 1
				break

			# kontrola jestli na konci pole je [ _ X X ]
			elif state[len(state) - 1] == "X" and state[len(state) - 2] == "X":
				move = len(state) - 3
				break

			# else:
			# 	if i+3 <= len(state) and state[i+3] != "X":
			# 		move = i + 3
			# 		break
			# 	else:
			# 		pass
	return move


def is_valid(move, state):
	for i in range(len(state)):
		if move <= len(state)-1 and state[move] != "X":
			return True
		else:
			print "Not a valid move!"
			return False


def victory_condition(state):
	for i in range(len(state) - 2):
		if state[i] == "X" == state[i + 1] == state[i + 2]:
			return True


def tictactoe(size, human_starts=True):
	if size < 3:
		print "size too small!"
		return None
	state = size * ['_']
	x = False
	if human_starts:
		turn = 0
	else:
		turn = 1
	while not x:
		valid = False
		if turn % 2 == 0:
			print "\nPlayer's turn"
			turn += 1
			while not valid:
				move = input("Insert your move: ")
				valid = is_valid(move, state)
		else:
			print "\nPC's turn"
			turn += 1
			move = strategy(state)
			print "PC put X on position ", move
		state[move] = "X"

		print " ".join(state)
		for i in range(len(state)):
			if i >= 10:
				i %= 10
			print i,
		print ""

		for i in range(len(state)):
			if i % 10 == 0:
				print i / 10,
			else:
				print " ",
		x = victory_condition(state)


tictactoe(26)
