import numpy as np 
from copy import copy


def f(x):
	'''
	Заданная функция
	Входные параметры:
	x - numpy.array. x[0] - x, x[1] - y
	'''
	return x[0]**4 + 2*(x[0]**2)*x[1] + 10*(x[0]**2) + 6*x[0]*x[1] + 10*(x[1]**2) - 6*x[0] + 4


def x_derivative(x):
	'''
	Частная производная функции по x
	'''
	return 4*(x[0]**3) + 4*x[0]*x[1] + 20*x[0] + 6*x[1] - 6


def y_derivative(x):
	'''
	Частная производная функции по y
	'''
	return 2*(x[0]**2) + 6*x[0] + 20*x[1]


def gradient_descent(a, eps):
	'''
	Функция градиентного спуска.
	Входные параметры:
	x_begin - начальные веса, тип - np.array
	alpha - скорость спуска
	eps - условие остановки
	'''
	x_prev = np.random.sample(2)  # Задаем случайные начальные параметры
	x = np.random.sample(2)
	for i in range(100000):
		if np.sum((x - x_prev)**2) < eps**2:  # Условие остановки
			pass
		x_prev = copy(x)
		x -= a*np.array([x_derivative(x_prev), y_derivative(x_prev)])  #Спускаемся в минимум
	return x 

x_min = gradient_descent(0.01, 0.00001)
print(x_min)
