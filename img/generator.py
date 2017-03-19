from PIL import Image
from os import remove
from sys import argv
screenshot = Image.new('RGBA', (400, 240 * 2))
pic1 = Image.open(argv[1])
pic2 = Image.open(argv[2])
screenshot.paste(pic1, (0,0))
screenshot.paste(pic2, (int(400 - 360), 240))
screenshot.save(argv[1].split("_")[1][0:4] + ".png")
remove(argv[1])
remove(argv[2])