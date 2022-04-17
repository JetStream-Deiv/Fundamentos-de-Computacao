import numpy as np
import matplotlib.pyplot as plt
import PIL
import cv2
from PIL import Image, ImageOps

from google.colab import files
upload = files.upload()

dogao = Image.open("dog.jpg")

doguinho = dogao.resize((100,100))

doguinho """imagem do animal já redimensionada"""

doguinhoReverso = doguinho.rotate(180)

doguinhoReverso """imagem do animal girada"""


"""carregar uma foto de um animal e girar 180o"""