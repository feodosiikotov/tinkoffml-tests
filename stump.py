class Stump:

	'''
	Класс решающего пня
	Описание алгоритма:
	Предположим, что мы уже нашли m.
	Тогда лучшее c1 - среднее арифметическое y, таких что, х, соответствующее этому y
	лежит до m
	Доказательство:
	Рассмотрим функцию потерь L(c1) = sum((c1 - y_i)**2).
	Ее производная равна sum(2(c1-y_i)). Cобой она представляет параболу,
	лежащую ветвями вверх, так что у нее один минимум
	Приравняем производную к нулю. n - количество y.
	Получим, что n*c1 = sum(y_i). Следовательно, минимум функции будет при 
	с1 = cреднему арифметическому. с2 доказывается аналогично
	Значения m можно разделить на несколько типов.
	1 - m меньше всех x
	2 - m больше всех x
	3 - m лежит между x_i и x_j, если они не равны
	Заметим, что случаи 1 и 2 аналогичны, так как либо c1 будет равно среднему арифм. всех значений у, либо с2, значения
	функции от этого не поменяются

	Следовательно перебираем m по двум случаям, считаем веса и потери и выбираем лучшие

	К сожалению, алгоритм имеет сложность О(n^2)

	'''

	def __init__(self, x_list, y_list):
		'''
		Параметры -  список х и список y
		'''
		self.input_data = sorted([(x_list[i], y_list[i]) for i in range(len(x_list))], key=lambda t: t[0])
		self.best_parameters = [None, None, None] # c1, c2, m
		self.best_loss =  None

	def training(self):
		'''
		Метод тренировки пня, алгоритм описан выше
		'''
		m = self.input_data[0][0] - 1
		c1, c2 = self.avg_index(len(self.input_data))
		self.best_parameters = [c1, c2, m]
		self.best_loss = self.count_loss(c1, c2, m)
		for i in range(len(self.input_data) - 1):
			if self.input_data[i][0] == self.input_data[i + 1][0]:
				continue
			else:
				m = (self.input_data[i][0] + self.input_data[i + 1][0])/2
				c1, c2 = self.avg_index(i + 1)
				loss = self.count_loss(c1, c2, m)
				print(c1, c2, m, loss)
				if loss < self.best_loss:
					self.best_loss = loss
					self.best_parameters = [c1, c2, m]




	def f(self, x, c1, c2, m):
		'''
		Заданная функция
		'''
		return c1 if x <= m else c2

	def count_loss(self, c1, c2, m):
		'''
		Функция потерь
		'''
		s = 0
		for pair in self.input_data:
			s += (self.f(pair[0], c1, c2, m) - pair[1])**2
		return s

	def avg_index(self, idx):
		'''
		Нахождение с1 и с2 по среднему значению частей массива, заданных по индексу
		'''
		c1 = 0
		for i in range(0, idx):
			c1 += self.input_data[i][1]
		c1 /= idx

		c2 = 0
		for i in range(idx, len(self.input_data)):
			c2 += self.input_data[i][1]
		if len(self.input_data) ==  idx:
			c2 = 0
		else:
			c2 /= (len(self.input_data) -  idx)

		return c1, c2






def main():
	print("Введите все x в одну строчку: ")
	x_list = list(map(int, input().split()))
	print("Введите все y в одну строчку: ")
	y_list = list(map(int, input().split()))
	model = Stump(x_list, y_list)
	model.training()
	print(model.best_parameters, model.best_loss)


if __name__ == "__main__":
	main()
