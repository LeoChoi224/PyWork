# 모델 & 스케일러 로드
import pandas as pd
import joblib

# 모델 로드
model_path = r'./model/iris_model.pkl'
clf = joblib.load(model_path)

# 스케일러 로드
model_path = r'./model/iris_scaler.pkl'
scaler = joblib.load(model_path)

# 예측 함수 작성
# 입력값: 웹에서 사용자가 입력한 값
# 출력값: 분류 문자열 (ex: Iris-setosa, Iris-versicolor, Iris-virginica)
def predict_iris(sepal_length, sepal_width, petal_length, petal_width) -> str:
    iris = pd.DataFrame(
            [[sepal_length, sepal_width, petal_length, petal_width]],
            columns=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'],
        )
    
    X_scaled = scaler.transform(iris)
    
    result = clf.predict(X_scaled)
    
    return result[0]





