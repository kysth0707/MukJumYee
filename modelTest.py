import cv2 as cv
import numpy as np
from keras.models import load_model
import tensorflow as tf
# from tensorflow.keras.preprocessing.image import load_img, img_to_array
# img_to_array(load_img(r'E:\GithubProjects\MukJumYee\testimg.png'))

TEXT_PATH='usedKors.txt'

model = load_model('mymodel.h5', compile=False)

model.compile(
	optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), # learning_rate 기본 값
	loss = 'sparse_categorical_crossentropy',
	# loss = 'categorical_crossentropy',
	metrics = ['accuracy'],
)

kors = []
with open(TEXT_PATH, 'r',encoding='utf8') as f:
	kors = f.readline()

mapObj = { x:i for i, x in enumerate(kors)}

def OneHotEncoding(data):
	ReturnObj = []

	ObjLen = len(mapObj)
	for label in data:
		temp = np.array([0. for _ in range(ObjLen)])
		temp[mapObj[label]] = 1.
		ReturnObj.append(temp)
	return np.array(ReturnObj)[0]

mapObjSwap = dict([(value, key) for key, value in mapObj.items()])

def OneHotDecoding(arr):
	maxPercent = 0
	result = "?"
	for i, percent in enumerate(arr):
		if percent > maxPercent:
			maxPercent = percent
			result = mapObjSwap[i]
	return (result, maxPercent)

def predict(img):
	result = model.predict(np.array([
		img
	]))

	return OneHotDecoding(result[0])

