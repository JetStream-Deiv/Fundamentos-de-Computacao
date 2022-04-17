import numpy as np
import matplotlib.pyplot as plt
import PIL
import cv2
from PIL import Image, ImageOps

from google.colab import files
upload = files.upload()

makima = Image.open("makima.jpg")

makima """para mostrar a imagem colorida"""

imagem_cinza = ImageOps.grayscale (makima)

imagem_cinza """para mostrar a imagem em escala cinza"""

"""carregue uma foto (colorida) e troque para escala de cinza"""