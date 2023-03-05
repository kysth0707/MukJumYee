import argparse
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import os
import time


def generate(option):
	print("폰트 이미지 생성을 시작합니다\n\n")
	FONT_PATH = option.font_path
	SAVE_PATH = option.save_path
	TEXT_PATH = option.text_path
	IMAGE_SIZE = option.image_size
	FONT_SIZE = option.font_size
	CSV_PATH = option.csv_path
	GAP = (IMAGE_SIZE - FONT_SIZE) * 2

	fonts = []
	for fontPos in os.listdir(FONT_PATH):
		fonts.append(ImageFont.truetype(f"{FONT_PATH}/{fontPos}", FONT_SIZE))
	fonts = np.array(fonts)

	kors = []
	with open(TEXT_PATH, 'r',encoding='utf8') as f:
		kors = f.readline()
	kors = np.array(list(kors))

	# 중간부터 시작
	# 맨 마지막 폴더는 삭제해야 됨
	# lastText = '탕'
	# kors = kors[kors.find(lastText) + 1:]
	# kors = np.array(list(kors))

	print(f"폰트 : {len(fonts)} 개 확인 됨")
	print(f"폰트 크기 : {FONT_SIZE}")
	print(f"저장 위치 : {SAVE_PATH}")
	print(f"텍스트 위치 : {TEXT_PATH} / {len(kors)} 개 확인 됨")
	print(f"이미지 크기 : {IMAGE_SIZE} X {IMAGE_SIZE}")
	# print(f"라벨링 저장 위치 : {CSV_PATH}")
	print(f"\n저장 위치({SAVE_PATH}) 가 비어있습니까? y 또는 n")
	if input() != "y":
		print(f"저장 위치({SAVE_PATH}) 를 비워주세요")
		return

	# with open(CSV_PATH, 'w',encoding='utf8') as f:
	# 	id = 0
	lastTime = time.time()
	korsLen = len(kors)
	for i, txt in enumerate(kors):
		print(f"\r{i + 1} / {korsLen} | {txt}   ", end='')
		if i == 2:
			print(f"\n{(time.time() - lastTime) * (len(kors) - i)} 초 예상됩니다\n")

		os.makedirs(f"{SAVE_PATH}/{txt}")
		# for gapY in range(0, int(GAP*0.5), 3):
		# 	for gapX in range(0, int(GAP*0.5), 3):
		# 		centerPos = (gapX, gapY)
		centerPos = (int((IMAGE_SIZE - FONT_SIZE)/2), int((IMAGE_SIZE - FONT_SIZE)/2))
		for ii, font in enumerate(fonts):
			img = Image.new(mode="L", size=(IMAGE_SIZE,IMAGE_SIZE), color=255)
			drawing = ImageDraw.Draw(img)
			drawing.text(
				centerPos,
				txt,
				fill=0,
				font=font,
			)
			for angle in range(-10, 11, 2):
				temp = img.rotate(angle, fillcolor=255)
				# temp.save(f'{SAVE_PATH}/{txt}/{ii}_{gapX}_{gapY}_{angle}.png')
				temp.save(f'{SAVE_PATH}/{txt}/{ii}_{angle}.png')
					
					# if id != 0:
					# 	f.write("\n")
					# f.write(f"{id},{SAVE_PATH}/{txt}/{ii}_{angle}.png,{txt}")
					# id += 1

		

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-font_path", type=str, default="./fonts")
	parser.add_argument("-save_path", type=str, default="./datasets")
	parser.add_argument("-text_path", type=str, default="./usedKors.txt")
	parser.add_argument("-image_size", type=int, default=32)
	parser.add_argument("-font_size", type=int, default=24)
	parser.add_argument("-csv_path", type=str, default="./labeling.csv")

	generate(parser.parse_args())