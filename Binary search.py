__author__ = 'Tomas'


# https://www.fi.muni.cz/IB111/sbirka/06-binarni_vyhledavani.html
# from random import randint
#
# def guess_number_human(upper_bound):
# 	the_number = randint(1, upper_bound)
# 	round = 0
# 	while True:
# 		round += 1
# 		print "----Round Number {}----".format(round)
# 		number = input("Zadej cislo")
# 		if the_number == number:
# 			print "Yes, that's my number!"
# 			break
# 		elif the_number > number:
# 			print "My number is bigger!"
# 		else:
# 			print "My number is smaller!"
#
#
#
# guess_number_human(10)

#
# from random import randint
#
#
# def guess_number_pc(upper_bound):
# 	while True:
# 		half = upper_bound / 2
# 		x = input("Is your number lower(0), equal(1) or higher(2) than {}".format(half))
# 		if x == 1:
# 			print "Your number is {}".format(x)
# 			break
# 		elif x == 0:
# 			upper_bound -= half
# 		elif x == 2:
# 			upper_bound += half
#
# guess_number_pc(10)


# Mysli si cislo od 1 do 10.
# Je cislo 5 mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?
# 2
# Je cislo 2 mensi (0), rovno (1), nebo vetsi (2) nez tvoje cislo?
# 2
# Tvoje cislo je 1.


# def caesar(text, n):
# 	new_string = ""
# 	for i in text:
# 		i = chr(ord(i) + n)
# 		if ord(i) == 32+n:
# 			new_string += " "
# 		elif ord(i) <= 122:
# 			new_string += i
# 		else:
# 			new_string += chr((ord(i)-122)+96)
# 			print ord(i)-(122+95)
# 	print ord(" ")
# 	return new_string
#
# print caesar('jedna dva tri', 18)
#
# def asdf(string):
# 	for i in string:
# 		print i + str(ord(i)),
#
# asdf("abcdefghijklmnopqrstuvwxyz")

# def vyhodnot(retezec):
# 	result = 0
# 	length = len(retezec)
# 	for i in retezec:
# 		if i == str("1") or i == str("0"):
# 			length -= 1
# 			result += int(i) * 2 ** length
# 		else:
# 			return 0
# 	return result
#
#
# print vyhodnot('11001')
# print vyhodnot('ru2vt')

# def presmycky(slovo1, slovo2):
# 	x = True
# 	if len(slovo1) == len(slovo2):
# 		for i in slovo1:
# 			if i in slovo2:
# 				x = True
# 			else:
# 				x = False
# 				break
#
# 	if x == True:
# 		print slovo1 + " a " + slovo2 + " jsou vzajemne presmycky"
# 	else:
# 		print slovo1 + " a " + slovo2 + " nejsou vzajemne presmycky"
#
#
# presmycky('utok', 'kota')
# # presmycky("asdg", "asdgjh")

# def cikcak(text):
# 	for i in range(len(text)):
# 		if i % 2 == 0:
# 			print text[i],
# 		else:
# 			print ".",
# 	print ""
# 	for j in range(len(text)):
# 		if j %2 != 0:
# 			print text[j],
# 		else:
# 			print ".",
#
#
#
# cikcak('PARDUBICE')
#
# def prvni_pismena(text):
# 	x = ""
# 	for i in text.split(" "):
# 		if len(i) < 1:
# 			x += " "
# 		else:
# 			x += i[0]
# 	return x
#
# print prvni_pismena('Ema mele maso  Ota vola ahoj')
#
# def velkex(n):
# 	start = 0
# 	finish = n
# 	for i in range(n+1):
# 		for j in range(n+1):
# 			if j == start or j == finish:
# 				print "#",
# 			else:
# 				print ".",
# 		print ""
# 		start += 1
# 		finish -= 1
#
#
# velkex(10)

# from random import randint

# PAVEL
# def pavel(n):
# 	ary = []
# 	for i in range(1, n+1):
# 		parent = randint(1,3)
# 		child = randint(1,3)
# 		policka = [child, parent]
# 		ary.append(policka)
# 	sort([
# 		[1, 1]
# 		[1, 1]
# 		[3, 1]
# 		[3, 2]
# 		[2, 3]
# 		[2, 1]])
#
# def sort(graph):
# 	for i in graph:
# 		for j in graph:
# 			if graph[i] < graph[j]:
# 				graph[j], graph[i] = graph[j], graph[i]
# 	print graph
#
#
# graph = {'1': [2],
# 		 '2': [0],
# 		 '3': [1],
# 		 '4': [1],
# 		 '5': [3],
# 		}
# sort(graph)
# PAVEL><