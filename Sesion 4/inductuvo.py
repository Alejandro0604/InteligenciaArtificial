from sklearn.linear_model import LinearRegression

X_train = [[1024], [2048], [3072], [4096], [5120], [6144], [7168], [8192]]

y_train = [1, 2, 3, 4, 5, 6, 7, 8]

model = LinearRegression()
model.fit(X_train, y_train)

kb = int(input("Ingrese el valor en kb: "))

kb_to_convert = [[kb]]
predict_mb = model.predict(kb_to_convert)

print (f"{kb} Kb equivalen aproximadamente a {predict_mb[0]} MB")