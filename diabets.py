import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model,datasets

diabetes = datasets.load_diabetes()

data_train = diabetes.data[:-20]
target_train = diabetes.target[:-20]
data_test = diabetes.data[-20:]
target_test = diabetes.target[-20:]

lin = linear_model.LinearRegression()
lin.fit(data_train,target_train)

print("Score:",lin.score(data_test,target_test))

predict = []
actual = []
for i in range(len(data_test)):
	print("Prediction:",lin.predict(data_test[i]))
	print("Actual value:",target_test[i])
	predict.append(lin.predict(data_test[i]))
	actual.append(target_test[i])

plt.plot(predict,color='r')
plt.plot(actual)
plt.show()