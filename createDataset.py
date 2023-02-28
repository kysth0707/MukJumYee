from PIL import Image, ImageFont, ImageDraw
from IPython.display import display
import os
import numpy as np
import time

BACKGROUND_COLOR = 255
FONT_COLOR = 0
FONT_SIZE = 48

IMAGE_WIDTH, IMAGE_HEIGHT = 64, 64
IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)

fonts = []
for fontPos in os.listdir("fonts"):
	fonts.append(ImageFont.truetype(f"./fonts/{fontPos}", FONT_SIZE))
fonts = np.array(fonts)

kors = []
with open("usedKors.txt", 'r',encoding='utf8') as f:
    kors = f.readline()
kors = np.array(list(kors))

lastTime = None
def startCheck():
	global lastTime
	lastTime = time.time()

def showPredictedTime(status, fullStatus):
	print(f"\n{(time.time() - lastTime) * fullStatus / status}초 예상\n")

def generateHanguelImages():

	startCheck()
	for i, txt  in enumerate(kors):
		print(f"\r{i + 1} / {len(kors)} | {txt}   ", end='')
		if i == 10:
			showPredictedTime(i, len(kors))

		for ii, font in enumerate(fonts):
			img = Image.new(mode="L", size=IMAGE_SIZE, color=BACKGROUND_COLOR)
			drawing = ImageDraw.Draw(img)
			drawing.text(
				((IMAGE_WIDTH - FONT_SIZE) / 2, (IMAGE_HEIGHT - FONT_SIZE) / 2),
				txt,
				fill=(FONT_COLOR),
				font=font,
			)
			for angle in range(-10, 11, 2):
				temp = img.rotate(angle, fillcolor=BACKGROUND_COLOR)
				temp.save(f'./datasets/{txt},{ii},{angle}.png')

if __name__ == "__main__":
	generateHanguelImages()