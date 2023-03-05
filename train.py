print("라이브러리를 불러오고 있습니다")
import os
import numpy as np
import tensorflow as tf
from model import getModel
from dataset import DataGenerator
from sklearn.model_selection import train_test_split
import argparse
from keras.models import load_model

def train(option):
	DATA_PATH = option.data_path
	NUM_CLASS = option.num_class
	IS_LOAD_MODEL = option.load_model
	MODEL_PATH = option.model_path
	CLASS_PATH = option.class_path
	EPOCHS = option.epochs

	kors = []
	with open(CLASS_PATH, 'r',encoding='utf8') as f:
		kors = f.readline()
	kors = np.array(list(kors))

	dataX = []
	dataY = []
	print("파일 위치를 불러오는 중 입니다")
	
	for i, txt in enumerate(os.listdir(f"{DATA_PATH}")):
		for file in os.listdir(f"{DATA_PATH}/{txt}"):
			dataX.append(f"{DATA_PATH}/{txt}/{file}")
			dataY.append(txt)
			print(f"\r{i+1} / {NUM_CLASS} ",end = '')

	dataX = np.array(dataX)
	dataY = np.array(dataY)

	trainX, validX, trainY, validY = train_test_split(dataX, dataY, test_size=0.05)
	trainDatagen = DataGenerator(trainX, trainY, kors)
	validDatagen = DataGenerator(validX, validY, kors)

	print(f"데이터 위치 : {DATA_PATH}")
	print(f"훈련 셋 : {len(trainX)} 개")
	print(f"검증 셋 : {len(validX)} 개")
	print(f"클래스 개수 : {NUM_CLASS}")
	print(f"모델 위치 : {MODEL_PATH}")
	print(f"훈련 세대 : {EPOCHS}")

	print("[ 모델을 ", end ='')
	print("로드함 ]" if IS_LOAD_MODEL else "로드하지 않음 ]")
	print("위 선택이 맞다면 y, 아니라면 n 을 작성해주세요")

	if input() != "y":
		print("종료합니다")
		return
	
	print("모델을 ", end ='')
	print("로드합니다" if IS_LOAD_MODEL else "로드하지 않습니다")

	if IS_LOAD_MODEL:
		model = load_model(MODEL_PATH)
	else:
		model = getModel(NUM_CLASS)
		model.summary()

	model.compile(
		optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), # learning_rate 기본 값
		loss = 'sparse_categorical_crossentropy',
		# loss = 'categorical_crossentropy',
		metrics = ['accuracy'],
	)

	model.fit(
		trainDatagen,
		epochs=EPOCHS,
		validation_data=validDatagen,
	)
	model.save(MODEL_PATH)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-data_path", type=str, default="./datasets")
	parser.add_argument("-class_path", type=str, default="usedKors.txt")
	parser.add_argument("-model_path", type=str, default="mymodel.h5")
	parser.add_argument("-load_model", dest="load_model", action="store_true")
	parser.add_argument("-num_class", type=int, default=2350)
	parser.add_argument("-epochs", type=int, default=20)
	# argparse.Namespace(data_path='./datasets', model_path='mymodel.h5', load_model=False, num_class=2350, epochs=20)
	train(parser.parse_args())