from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (500, 300), (128, 0, 128))

draw = ImageDraw.Draw(image)


text = input("Anna lause, joka piirretään kuvan alanurkkaan: ")

font = ImageFont.truetype("arial.ttf", 20)

text_position = (50, 250)
draw.text(text_position, text, fill=(255, 165, 0), font=font)


triangle_points = [(250, 50), (200, 150), (300, 150)]
draw.polygon(triangle_points, fill=(255, 255, 255))

# Yritetään piirtää sininen ympyrä kolmion sisälle
circle_center = (250, 120)  # Ympyrän keskikohta
circle_radius = 25  # Ympyrän säde
draw.ellipse(
    [(circle_center[0] - circle_radius, circle_center[1] - circle_radius),
     (circle_center[0] + circle_radius, circle_center[1] + circle_radius)],
    fill=(0, 0, 255)
)

# Tallennetaan kuva tiedostoon
image.save("output_image1.png")

# Näytetään kuva
image.show()
