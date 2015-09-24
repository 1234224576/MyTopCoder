import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as datasets
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

iris = datasets.load_iris()

data = iris.data[iris.target != 2]
target = iris.target[iris.target != 2]

logi = LogisticRegression()
logi.fit(data,target)

plt.plot(logi.predict(data))
plt.plot(target)
plt.show()
# scores = cross_validation.cross_val_score(logi,data,target,cv=5)
# print(scores)