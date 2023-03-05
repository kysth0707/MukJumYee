import os
import tensorflow as tf
import math
import numpy as np
import copy
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# tensorflow -> keras -> utils -> Sequence 주석
"""Base object for fitting to a sequence of data, such as a dataset.
데이터 세트와 같은 데이터 시퀀스에 맞추기 위한 기본 개체입니다.

Every `Sequence` must implement the `__getitem__` and the `__len__` methods.
모든 `Sequence`는 `__getitem__` 및 `__len__` 메서드를 구현해야 합니다.
If you want to modify your dataset between epochs you may implement
시대 사이에 데이터 세트를 수정하려면 다음을 구현할 수 있습니다.
`on_epoch_end`.
`on_epoch_end`.
The method `__getitem__` should return a complete batch.
메소드 `__getitem__`은 완전한 배치를 반환해야 합니다.

Notes:
노트:

`Sequence` are a safer way to do multiprocessing. This structure guarantees
that the network will only train once
	on each sample per epoch which is not the case with generators.
'시퀀스'는 다중 처리를 수행하는 더 안전한 방법입니다. 
이 구조는 생성기의 경우가 아닌 Epoch당 각 샘플에서 네트워크가 한 번만 훈련되도록 보장합니다.

Examples:
예시들:

```python
from skimage.io import imread
from skimage.transform import resize
import numpy as np
import math

# Here, `x_set` is list of path to the images
# 여기서 `x_set`은 이미지의 경로 목록입니다.
# and `y_set` are the associated classes.
# 및 `y_set`은 연관된 클래스입니다.

class CIFAR10Sequence(tf.keras.utils.Sequence):

	def __init__(self, x_set, y_set, batch_size):
		self.x, self.y = x_set, y_set
		self.batch_size = batch_size

	def __len__(self):
		return math.ceil(len(self.x) / self.batch_size)

	def __getitem__(self, idx):
		batch_x = self.x[idx * self.batch_size:(idx + 1) *
		self.batch_size]
		batch_y = self.y[idx * self.batch_size:(idx + 1) *
		self.batch_size]

		return np.array([
			resize(imread(file_name), (200, 200))
				for file_name in batch_x]), np.array(batch_y)
```
"""

class DataGenerator(tf.keras.utils.Sequence):
	def __init__(self, dataX, dataY, classes, batchSize = 256, shuffle = True) -> None:
		self.x, self.y = dataX, dataY
		# self.batchSize = math.floor(len(self.x) / batchSize)
		self.batchSize = batchSize
		self.numSamples = len(dataX)

		self.classes = classes
		self.char2index = {char : i for i, char in enumerate(self.classes)}
		# standardArr = np.array([0.] * self.numClasses)
		# for i, char in enumerate(np.unique(dataY)):
		# 	arr = copy.deepcopy(standardArr)
		# 	arr[i] = 1.
		# 	self.char2index[char] = arr

		self.numClasses = len(self.classes)

		self.shuffle = shuffle
		self.on_epoch_end()
		print(f"{len(self.x)} 이미지가 로딩 됨")

	def __len__(self):
		return math.floor(self.numSamples / self.batchSize)
	
	def __getitem__(self, index):
		indices = self.indices[index * self.batchSize : (index + 1) * self.batchSize]
		posX = [self.x[i] for i in indices]
		batchY = [self.char2index[self.y[i]] for i in indices]
		batchX = []
		for pos in posX:
			x = load_img(pos, target_size = (32, 32))
			x = img_to_array(x)
			x = x / 255.
			batchX.append(x)
		# print("\n\n\n\n\n")
		# print(indices)
		# print(batchX[0].shape)
		# print("\n\n\n\n\n")

		return np.array(batchX), np.array(batchY)
	
	def on_epoch_end(self):
		self.indices = np.arange(self.numSamples)
		if self.shuffle:
			np.random.shuffle(self.indices)