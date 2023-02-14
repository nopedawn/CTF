from PIL import Image

width = None
height = None
data = []
with open("somedata.txt") as f:
    for line in f:
        x, y = map(int, line.split(","))
        data.append((x, y))
        if width is None or x > width:
            width = x
        if height is None or y > height:
            height = y

width += 20
height += 20
image = Image.new("RGB", (width, height), (255, 255, 255))
pixels = image.load()

for point in data:
    pixels[point[0]+5, point[1]+5] = (0, 0, 0)

image = image.resize((500,500), Image.NEAREST)
image.save("output.png")