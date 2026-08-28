import numpy as np
from tensorflow import keras
from PIL import Image

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# 학습 모델 로딩.
model_path = r'./model/best-cifar10-deepcnn.keras'
model = keras.models.load_model(model_path)

def predict_images(file_paths):
    data_list = []

    for file_path in file_paths:
        img = Image.open(file_path)
        rgb_img = img.convert('RGB')
        resize_img = rgb_img.resize((32, 32))
        data_list.append(np.array(resize_img))

    data_arr = np.array(data_list)
    data_scaled = data_arr / 255.0

    preds = model.predict(data_scaled)

    return [class_names[i] for i in np.argmax(preds, axis=1)]