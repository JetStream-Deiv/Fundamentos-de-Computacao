import numpy as np
import matplotlib.pyplot as plt
import PIL
import cv2

from google.colab import files
upload = files.upload()

im=plt.imread("MarriageStory.jpg")
plt.imshow(im) """para certificar que a imagem é colorida"""

plt.imshow(im[:,:,0], cmap = 'gray')

"""Carregue uma foto sua no python (deixe o eixo)"""