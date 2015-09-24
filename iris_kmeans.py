import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(10)
X = np.r_[np.random.randn(30,2) + [2,-2],
		  np.random.randn(30,2) + [0,-2],
		  np.random.randn(30,2) + [-2,2]]

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
makers = ["o","v","x"]
for i in range(3):
	xx = X[kmeans.labels_ == i]
	plt.scatter(xx[:,0],xx[:,1],c="k",marker=makers[i])
plt.show()