from flask import Flask, render_template, Response
import cv2
import numpy as np
from keras.models import load_model
from PIL import ImageOps

app = Flask(__name__)

# Carregar o modelo
model = load_model("keras_model.h5", compile=False)
# Carregar os rótulos
class_names = open("labels.txt", "r").readlines()

def detect_leakage(frame):
    # redimensionando o frame para ter pelo menos 224x224 e depois cortando do centro
    frame = cv2.resize(frame, (224, 224))
    # transformar o frame em um array numpy
    image_array = np.asarray(frame)
    # Normalizar o frame
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    # Criar o array da forma certa para alimentar o modelo keras
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    # Predição do modelo
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name, confidence_score

