# def test(x, y):
# 	diff=x-y
# 	if x > y:
# 		print "{} je vetsi nez {} o {}".format(x, y, diff)
# 	elif x == y:
# 		print "Cisla jsou si rovna"
# 	else:
# 		test(y, x)
#
#
# test(2,5)
# test(8,-5)
# test(9,9)
#
# def tabulka(n):
# 	zac = n + 1
# 	for i in range(1, zac):
# 		f = n + 2 - zac
# 		for z in range(f, 1, -1):
# 			print z,
# 		for j in range(1, zac):
# 			print j,
#
# 		print ""
# 		zac -= 1
# tabulka(7)


#  1 2 3 4 5 6 7
#  2 1 2 3 4 5 6
#  3 2 1 2 3 4 5
#  4 3 2 1 2 3 4
#  5 4 3 2 1 2 3
#  6 5 4 3 2 1 2
#  7 6 5 4 3 2 1


#
# def pismenoh(n):
# 	for i in range(n):
# 		if i == n/2:
# 			print n* "#"
# 		else:
# 			print "#" + (n-2)* "." + "#"
#
#
#
# pismenoh(5)
# pismenoh(6)
#
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
#
# string_intersection('ZIRAFA', 'KARAFA')
#
# from random import randint
#
# def randoms(n):
# 	sez = []
# 	avg = 0
# 	ssez = []
# 	for i in range(n+1):
# 		sez.append(randint(1,100))
# 	for j in sez:
# 		avg += j
# 	avg /= n
# 	print avg
# 	for z in sez:
# 		if z > avg:
# 			ssez.append(z)
# 	print sez
# 	print sorted(ssez)
#
#
#
#
# randoms(15)
#
# def tree(n):
# 	space = n/2-1
# 	twig= 3
# 	for i in range(1, n + 1):
# 		if i % 2 != 0:
# 			print (n / 2) * " " + "#"
# 		else:
# 			print space* " " + twig*"#"
# 			space -= 1
# 			twig+= 2
# tree(9)
#
# def fib(n):
# 	x = 0
# 	y = 1
# 	z = 0
# 	for i in range(n):
# 		z = x + y
# 		x = y
# 		y = z
# 		print z,
# 	print ""
#
#
# fib(8)



# REKURZE


# def fib(x, y, numb):
# 	result = x + y
# 	print result,
# 	if numb != 1:
# 		numb -= 1
# 		fib(y, result, numb)
#
#
# fib(0, 1, 8)
