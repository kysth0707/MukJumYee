print("라이브러리를 불러오고 있습니다")
import os
import numpy as np
import tensorflow as tf
from model import getModel
from dataset import DataGenerator
from sklearn.model_selection import train_test_split

def train():
	DATA_PATH = r"E:\GithubProjects\MukJumYee\datasets"
	NUM_CLASS = 2350
	dataX = []
	dataY = []
	print("파일 위치를 불러오는 중 입니다")
	
	for txt in os.listdir(f"{DATA_PATH}"):
		for file in os.listdir(f"{DATA_PATH}/{txt}"):
			dataX.append(f"{DATA_PATH}/{txt}/{file}")
			dataY.append(txt)

	dataX = np.array(dataX)
	dataY = np.array(dataY)

	trainX, validX, trainY, validY = train_test_split(dataX, dataY, test_size=0.01)

	trainDatagen = DataGenerator(trainX, trainY)
	validDatagen = DataGenerator(validX, validY)



	model = getModel(NUM_CLASS)
	model.summary()

	model.compile(
		optimizer = tf.keras.optimizers.Adam(learning_rate=0.001), # learning_rate 기본 값
		loss = 'sparse_categorical_crossentropy',
		metrics = ['acc'],
	)

	model.fit(
		trainDatagen,
		epochs=10,
		validation_data=validDatagen,
		batch_size=128
	)


if __name__ == "__main__":
	train()