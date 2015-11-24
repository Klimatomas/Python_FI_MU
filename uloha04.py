from random import randint

__author__ = 'Tomas'


def strategy(state):
	for i in range(len(state)):
		valid = False
		if state[i] == "X":
			#  kdyz hrac zahral na posledni nebo predposledni pole v prvnim tahu
			#  zahraje pocitac na nahodne pole ktere je mimo dosah.
			if i >= len(state) - 2:
				while not valid:
					move = randint(0, i - 3)
					valid = is_valid(move, state)
					break
			else:
				# kontrola stavu [ X X _ ], jestlize pocitac vidi tento stav, ukonci hru vyhrou.
				if state[i + 1] == "X":
					move = i + 2
					break

				# kontrola stavu [ X _ X ] jestlize pocitac vidi tento stav, ukonci hru vyhrou.
				elif state[i + 2] == "X":
					move = i + 1
					break

				# kontrola jestli na konci pole je [ _ X X ], jestlize ano, ukonci hru vyhrou.
				elif state[-1] == "X" and state[-2] == "X":
					move = len(state) - 3
					break
				# kontroluje jesli svym tahem nenahrava hraci.
				elif i + 3 <= len(state) - 1 and state[i + 3] != "X":
					if i + 5 <= len(state) - 1 and (state[i + 4] == "X" or state[i + 5] == "X"):
						pass
					else:
						move = i + 3
						break
				# jestlize vyse uvedene podminky nejsou splneny, ale prvni tri pole jsou volna, umisti X na prvni pole.
				elif state[0] == state[1] == state[2]:
					move = 0
					break
		else:
			while not valid:
				# jestlize nenasel zadnou z vyse uvedenych podminek, je jedno jak zahraje
				# zahraje tedy nahodny validni tah.
				move = randint(0, len(state) - 1)
				valid = is_valid(move, state)

	return move


def is_valid(move, state, player=False):
	for i in range(len(state)):
		if move <= len(state) - 1 and state[move] != "X":
			return True
		else:
			if player:
				print "Neplatny pohyb!"
			return False


def victory_condition(state):
	for i in range(len(state) - 2):
		if state[i] == "X" == state[i + 1] == state[i + 2]:
			return True


def print_state(state):
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


def tictactoe(size, human_starts=True):
	if size <= 3:
		print "size too small!"
		return None
	state = size * ['_']
	end = False
	if human_starts:
		turn = 0
	else:
		turn = 1
	while not end:
		print_state(state)
		valid = False
		if turn % 2 == 0:
			print "\nNa tahu: hrac"
			turn += 1
			while not valid:
				move = input("Zadej tah: ")
				valid = is_valid(move, state, True)
		else:
			print "\nNa tahu: pocitac"
			turn += 1
			move = strategy(state)
			print "Zahral na pozici: ", move
		state[move] = "X"
		end = victory_condition(state)

	print_state(state)
	if turn % 2 == 0:
		print "\nProhral jsi!"
	else:
		print "\nVyhral jsi!"


tictactoe(10)