# Base para la solución del Laboratorio 4

# Los parámetros T, t_final y N son elegidos arbitrariamente

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math

# Variables aleatorias A y B
vaA = stats.norm(3, np.sqrt(10))
vaB = stats.norm(3, np.sqrt(10))

# Definimos wo como un valor razonable
wo=2*np.pi

# Creación del vector de tiempo
T = 100			# número de elementos
t_final = 10	# tiempo en segundos
t = np.linspace(0, t_final, T)

# Inicialización del proceso aleatorio W(t) con N realizaciones
N = 10
W_t = np.empty((N, len(t)))	# N funciones del tiempo x(t) con T puntos

# Creación de las muestras del proceso w(t) (A y B independientes)
for i in range(N):
	X = vaA.rvs()
	Y = vaB.rvs()
	w_t = ((X * np.cos(wo*t))+ (Y*np.sin(wo*t)))
	W_t[i,:] = w_t
	plt.plot(t, w_t)

#Definimos  varianzas iguales sigma^2 o E[X^2] ya que E^2[X]=0
xquad= math.pow(X, 2)
sigma= np.mean(xquad)

# Promedio de las N realizaciones en cada instante (cada punto en t)
P = [np.mean(W_t[:,i]) for i in range(len(t))]
plt.plot(t, P, lw=6)

# Graficar el resultado teórico del valor esperado, como EX y EY son 0 se puede ver como
E = 0*t
plt.plot(t, E, '-.', lw=4)


# Mostrar las realizaciones, y su promedio calculado y teórico
plt.title('Realizaciones del proceso aleatorio $W(t)$')
plt.xlabel('$t$')
plt.ylabel('$w_i(t)$')
plt.show()

# T valores de desplazamiento tau
desplazamiento = np.arange(T)
taus = desplazamiento/t_final

# Inicialización de matriz de valores de correlación para las N funciones
corr = np.empty((N, len(desplazamiento)))

# Nueva figura para la autocorrelación
plt.figure()

# Cálculo de correlación para cada valor de tau
for n in range(N):
	for i, tau in enumerate(desplazamiento):
		corr[n, i] = np.correlate(W_t[n,:], np.roll(W_t[n,:], tau))/T
	plt.plot(taus, corr[n,:])

# Valor teórico de correlación, se saca de la solucion del problema
Rww = sigma*np.cos(wo*taus)

# Gráficas de correlación para cada realización
plt.plot(taus, Rww, '-.', lw=4, label='Correlación teórica')
plt.title('Funciones de autocorrelación de las realizaciones del proceso')
plt.xlabel(r'$\tau$')
plt.ylabel(r'$R_{WW}(\tau)$')
plt.legend()
plt.show()
