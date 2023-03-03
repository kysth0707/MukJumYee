from PIL import Image, ImageFont, ImageDraw
from IPython.display import display
import copy
import numpy as np
import cv2 as cv

topPos = r'E:\GithubProjects\MukJumYee'
backgroundColor = (255, 255, 255)
fontColor = (0, 0, 0)

def loadFont(ttfPos : str, fontSize : int = 20):
	return ImageFont.truetype(font=ttfPos, size=fontSize)

fonts = {
	'바탕체' : loadFont(fr"{topPos}\fonts\batang.ttc"),
	'고딕체' : loadFont(fr"{topPos}\fonts\Hancom Gothic Regular.ttf"),
	'고딕체-굵음' : loadFont(fr"{topPos}\fonts\Hancom Gothic Bold.ttf"),
	'굴림체' : loadFont(fr"{topPos}\fonts\gulim.ttc"),
}

def drawText(targetImage, text, font, fontPos):
	out = ImageDraw.Draw(targetImage)
	out.text(fontPos, text, fontColor, font)
	return targetImage

def getImage(text, font, imgSize = (30, 30), fontPos = (5, 5), rotateAngle = 0):
	font = fonts.get(font)
	if font == None:
		font = fonts['바탕체']
	img = Image.new(mode="RGBA", size=imgSize, color=backgroundColor)
	drawText(img, text, font, fontPos)
	img = np.asarray(img)
	if rotateAngle == 0:
		return img
	else:
		return Rotate(img, rotateAngle)

def Rotate(ResultImage, angle):
	ResultImage = copy.deepcopy(ResultImage)
	image_center = tuple(np.array(ResultImage.shape[1::-1]) / 2)
	rot_mat = cv.getRotationMatrix2D(image_center, angle, 1.0)
	ResultImage = cv.warpAffine(ResultImage, rot_mat, ResultImage.shape[1::-1], flags=cv.INTER_LINEAR)
	return ResultImage