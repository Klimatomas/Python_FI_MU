from PIL import Image


def obr_values(width, height, x, y, image, radius):
	r = 0
	g = 0
	b = 0
	count = 0
	for i in range(-radius, radius+1):
		for j in range(-radius, radius+1):
			count += 1
			if x+i >= width or x+i < 0:
				pass
			elif y+j >= height or y+j < 0:
				pass
			elif (x+i - radius) ** 2 + (y+j - radius) ** 2 > radius ** 2:
				red, green, blue = image.getpixel((x+i, y+j))
				r += red
				g += green
				b += blue
			else:
				count += 1

	return r / count, g / count, b / count


def obr(filename, radius=4):
	image = Image.open(filename)
	image.convert("RGB")
	width, height = image.size
	for x in range(width):
		for y in range(height):
			r, g, b = obr_values(width, height, x, y, image, radius)
			image.putpixel((x, y), (r, g, b))

	image.show()


obr("1.jpg", 0)
