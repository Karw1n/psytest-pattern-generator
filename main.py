from PIL import Image, ImageDraw


width, height = 200, 200
centre_x, centre_y = width // 2, height // 2
radius = 50
top_left = (centre_x - radius, centre_y - radius)
bottom_right = (centre_x + radius, centre_y + radius)

impage_pillow = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(impage_pillow)

draw.ellipse([top_left, bottom_right], fill="black")

impage_pillow.show()