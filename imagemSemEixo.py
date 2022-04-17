import numpy as np
import matplotlib.pyplot as plt
import PIL
import cv2

from google.colab import files
upload = files.upload()

makima=plt.imread("makimadoguineo.jpg")

plt.imshow(makima)
plt.xticks([], [])
plt.yticks([], [])

"""Carregue uma foto no python e tire o eixo x e o eixo y"""