import pandas as pandas
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler
import joblib as joblib
import numpy as np

# Зареждане на данни
data = pandas.read_csv("data.csv")

# Разделяне на данните на признаци и целева променлива
x = data[['AirTemp', 'Press', 'UMR']]
y = data[['NO', 'NO2', 'O3', 'PM10']]

# Разделяне на данните на обучителен и тестов набор
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# Скалиране на признаците
scaler = RobustScaler()
scaler.fit(x_train)
x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

# Запазване на скалиращия обект
joblib.dump(scaler, 'scaler.joblib')

# Обучаване на модела за Ridge регресия
clf = Ridge(alpha=1.0,
            solver='auto',
            fit_intercept=True,
            copy_X=True,
            max_iter=None,
            tol=0.001)
clf.fit(x_train_scaled, y_train)

# Запазване на обучения модел
joblib.dump(clf, 'clf.joblib')

# Оценка на модела върху тестовите данни
print("Score: ", clf.score(x_test_scaled, y_test))

# Пример за предсказване с модела
arr = np.array([[25, 955, 80]])
arr_scaled = scaler.transform(arr)
print("Predict: ", clf.predict(arr_scaled))



