from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples = 100, centers = 4, cluster_std = 1.5)
plt.scatter(X[:,0], X[:,1])

model = KMeans(n_clusters=4, n_init = 15, max_iter = 200)

model.fit(X)
model.predict(X)
plt.scatter(X[:,0], X[:,1], c= model.predict(X))