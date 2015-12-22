# -*- coding: utf-8 -*-

# from PIL import Image
#
#
# def obr_values(width, height, x, y, image, radius):
# 	r = 0
# 	g = 0
# 	b = 0
# 	count = 0
# 	for i in range(-radius, radius+1):
# 		for j in range(-radius, radius+1):
# 			count += 1
# 			if x+i >= width or x+i < 0:
# 				pass
# 			elif y+j >= height or y+j < 0:
# 				pass
# 			elif (x+i - radius) ** 2 + (y+j - radius) ** 2 > radius ** 2:
# 				red, green, blue = image.getpixel((x+i, y+j))
# 				r += red
# 				g += green
# 				b += blue
# 			else:
# 				count += 1
#
# 	return r / count, g / count, b / count
#
#
# def obr(filename, radius=4):
# 	image = Image.open(filename)
# 	image.convert("RGB")
# 	width, height = image.size
# 	for x in range(width):
# 		for y in range(height):
# 			r, g, b = obr_values(width, height, x, y, image, radius)
# 			image.putpixel((x, y), (r, g, b))
#
# 	image.show()
#
#
# obr("1.jpg", 0)


# TODO prepsat ty jmena funkci n shit

import re


# print line.decode('utf-8')
# class NameAnalyser(object):
#     def __init__(self):
#         pass
#
#
# def main():
#     input_file = open("krestni_jmena.csv", "r")
#     content = input_file.readlines()
#     string = ''.join(content)
#     print (re.match(r'[^,]\D\w*\s?\w*', string))
#     # print names.group()
#
#
#
# main()

# -*- coding: utf-8 -*-
__author__ = 'KLIM028'

import re


# print line.decode('utf-8')
# class NameAnalyser(object):
#     def __init__(self):
#         pass
#
#
# def main():
#     input_file = open("krestni_jmena.csv", "r")
#     content = input_file.readlines()
#     string = ''.join(content)
#     print (re.match(r'[^,]\D\w*\s?\w*', string))
#     # print names.group()
#
#
#
# main()

class NameAnalyser(object):
	def __init__(self, name, properties):
		self.name = name
		self.properties = properties


def main(file_name):
	names = []
	data = []
	years = []
	occurence = []
	x = 0
	with open(file_name) as f:
		lines = f.read().split('\n')  # nacteme všechny radky do seznamu
		string = "".join(lines)
		for line in lines:
			name = line.split(",")
			names.append(name[0])
			x = len(name)
			# print name.decode('utf-8')
			for i in range (1, len(name)):
				data.append(name[i])
	for j in range(1, x-1):
		years.append(data[j])


	# print data[120]
	print years


main("krestni_jmena.csv")
#
# def krestni_jmena(jmeno_souboru):
# f = open(jmeno_souboru)
# jmena = []
# for radek in f.readlines():
# m = re.match(r’\d+\.;\d+;"\w+, (\w+)’, radek)
# if m: jmena.append(m.group(1))
# jmena.sort()
# print " ".join(jmena)
# f.close()
