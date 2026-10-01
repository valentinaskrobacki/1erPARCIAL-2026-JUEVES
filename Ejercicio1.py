N = 5 #cantidad de donas/pasos

donas = [(2**0.5) ** (i - 1) for i in range(1, N + 1)] #uso 2**0.5 porque representa la raiz de 2

print(donas)