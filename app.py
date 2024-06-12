from flask import Flask, render_template, Response
import cv2
import numpy as np
from keras.models import load_model
from PIL import ImageOps

app = Flask(__name__)
