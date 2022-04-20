import matplotlib.pyplot as plt

A = float(input("Insira o valor de (A): "))

B = float(input("Insira o valor de (B): "))

X = float(input("insira o valor de X: "))

Y = (A * X) + B

print("valor do calculo: ", Y)

x1 = (X, 0)
y1 = (Y, 0)

plt.plot(x1, y1)
plt.show()
