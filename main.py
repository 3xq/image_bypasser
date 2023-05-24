from PIL import	Image

base_xml = open('image.rbxmx', encoding='utf-8', errors='ignore').read()

image = Image.open('test.jpg')
image = image.resize((128, 96))

pixels = image.load()

width, height = image.size
image_data = 'local image = {'

for y in range(height):
	row = f"    [{y}] = '"

	for x in range(width):
		row = row + f'<stroke color="rgb{str(pixels[x, y])}"><font color="rgb{str(pixels[x, y])}">□</font></stroke>'

	row = row + "',"

	image_data = image_data + '\n' + row

image_data = image_data + '\n}'
image_data = image_data + '\n\nreturn image'

base_xml = base_xml.replace('___', image_data)

open('new_image.rbxmx', 'w', encoding='utf-8').write(base_xml)
