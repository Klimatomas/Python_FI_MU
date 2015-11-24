__author__ = 'Tomas'


# Vypiste znaky ktere jsou na stejnych pozicich dvou stringu stejne
# def string_intersection(left, right):
# 	result = ''
# 	if len(left) > len(right):
# 		shorter_one = len(right)
# 	else:
# 		shorter_one = len(left)
#
# 	for i in range(shorter_one):
# 		if left[i] == right[i]:
# 			result += left[i]
# 	print result
#
# string_intersection('ZIRAFA', 'KARAFA')
# # R A F A
# string_intersection('PES', 'KOCKA')
#
# string_intersection('asdfghjkl', 'axcvbhjk')
#
# # (prazdny retezec)


# Vrati true jestlize je slovo palindrom, jestlize neni, vrati false
# def palindrom(text):
# 	if text == text[::-1]:
# 		return True
# 	else:
# 		return False
#
#
# print palindrom("JELENOVIPIVONELEJ")
# print palindrom("ABRAKADABRA")
# # True


# vratte hodnotu slova, kdyz pismeno ma hodnotu jeho pozice v abecede
# def word_value(text):
# 	result = 0
#
# 	for i in text:
# 		result +=(ord(i)-64)
# 		print "hodnota {} je {}".format(i, ord(i))
# 	return result
#
#
# print word_value("AHOJ")
# # 34

# pokud je hodnota predchozich dvou pismen rovna pismenu potom skrtni pismeno
# def strange_filter(text):
# 	value = 0
# 	prev_value = 0
# 	new_str = ''
# 	for i in range(len(text)):
# 		pprev_value = prev_value
# 		prev_value = value
# 		value = ord(text[i]) - 64
# 		if pprev_value + prev_value == value:
# 			pass
# 		else:
# 			new_str += text[i]
# 	return new_str
#
#
# print strange_filter("ABCDEIGHO")
# ABDEGH


# nahodny retezec - dostanes retezec znaku a delku vysledneho stringu, udelej random string
# from random import randint
#
#
# def random_string(length, chars):
# 	str = ''
# 	while len(str) < length:
# 		str += chars[randint(0, len(chars) - 1)]
# 	return str
#
#
# print random_string(10, "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

# najdi substring ve stringu a vypis index pocatku else vypis -1
# def search(needle, haystack):
# 	start = 0
# 	end = len(needle)
# 	while True:
# 		if haystack[start:end] == needle:
# 			print "omfg sem tam"
# 			return start
# 		elif len(haystack) < end:
# 			return -1
# 		start += 1
# 		end += 1
# 	# haystack.find(needle)
#
#
# print search("tri", "bratri")
# # 3


def tuple_reverse(text, n):
	final = ''
	step = n
	x = 0
	while len(text) != len(final):
		final += text[x:n][::-1]
		x += step
		n += step
	return final


print tuple_reverse('HESLOJETAJEMNO', 3);
# SEHJOLATEMEJON
