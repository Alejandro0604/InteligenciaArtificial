from sklearn.neighbors import NearestNeighbors
import numpy as np

X_train = np.array([[1, 2], [2,3], [3, 4], [4, 5], [5, 6]])

X_unknown = np.array([[1.5, 2.5], [3.5, 4.5]])

model = NearestNeighbors(n_neighbors=2)
model.fit(X_train)

distances, indices = model.kneighbors(X_unknown)

for i in range(len(X_unknown)):
    print("Para la observación", X_unknown[i], " los vecinos más cercanos son:", X_train[indices[i]])