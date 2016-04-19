import tensorflow.contrib.learn as skflow
import tensorflow.contrib.learn as skflow
from sklearn import datasets, metrics
from sknn.mlp import Classifier, Layer
import pandas as pd
import numpy as np


data = pd.read_csv("~/Desktop/TextMining/data/features_tfidf_d_train.csv")
data[0:2]

import random
rows = random.sample(data.index, 25000)
train_data = data.ix[rows]
test_data = data.drop(rows)

y_train = train_data["relevance"]
x_train = train_data.drop(['relevance','id'],1)

y_test = test_data["relevance"]
x_test = test_data.drop(['relevance','id'],1)


regressor = skflow.TensorFlowDNNRegressor(hidden_units=[30, 50],
	steps=5000, learning_rate=0.1, batch_size=1)

regressor.fit(x_train, y_train)

y_hat = regressor.predict(x_train)





