from PIL import Image

img = Image.open("testing files\Munchkin_Loot_Letter_base.jpg")
img.thumbnail((500,500))
img.save("test.jpg")
img.close