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
