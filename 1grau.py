import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

# Em cima está importado o tkinter, e embaixo está criando o objeto "WINDOW".
WINDOW = tk.Tk()
# Para remover a interface da tela do usuário sem "destruí-la"
WINDOW.withdraw()
# Dialogo de INPUT para o usuario
A = simpledialog.askfloat(title="Valores da Funcao",
                          prompt="Insira o valor de (A): ")

B = simpledialog.askfloat(title="Valores da Funcao",
                          prompt="Insira o valor de (B): ")

X = simpledialog.askfloat(title="Valores da Funcao",
                          prompt="Insira o valor de (X): ")
# Metodo askfloat é apenas para pegar o valor numerico inserido

Y = (A * X) + B

# para testar se a conta está correta.
# No print abaixo, também foi utilizado o f string
print(f'valor do calculo: {Y:.2f}')

x1 = (X, 0)
y1 = (Y, 0)

plt.plot(x1, y1)
plt.show()
