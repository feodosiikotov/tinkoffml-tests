import numpy as np
import os
from copy import deepcopy
from time import sleep

#Константы для графического отображения игры
shrimp = 'S'
fish = '0'
rock = '#'
empty = '.'


def cls():
	'''
	Функция для очистки консоли
	'''
	os.system('cls' if os.name == 'nt' else 'clear')


def field_gen(n, m):
	'''
	Функция для изначальной генерации игрового поля
	'''
	return np.random.choice([shrimp, fish, rock, empty], (n, m), p=[0.4, 0.4, 0.05, 0.15])


def field_draw(field, mode):
	'''
	Функция для отрисовки поля
	'''
	cls()
	if mode == 1:
		sleep(1)
	for i in field:
		print(*i, sep=' ')

def neighbours_gen(field, x, y):
	'''
	Генерация списка соседей клетки, заданной по координатам
	'''
	neighbours = []
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			if i != x or j != y :
				if i != -1 and j != -1 and i != len(field) and j != len(field[0]):
					neighbours.append(field[i][j])
	return neighbours

def is_dying(neighbours, creature):
	'''
	Вычисляет по количеству соседей умирает ли рыба или креветка
	'''
	if neighbours.count(creature) >= 4 or neighbours.count(creature) < 2:
		return True
	return False



def move(field, n, m):
	'''
	Функция для изменения состояния поля
	'''
	new_field = deepcopy(field)
	for i in range(n):
		for j in range(m):
			if field[i][j] == rock:
				new_field[i][j] = rock
			else:
				neighbours = neighbours_gen(field, i, j)
				if field[i][j] == fish or field[i][j] == shrimp:
					if is_dying(neighbours, field[i][j]):
						new_field[i][j] = empty
				else:
					if neighbours.count(fish) == 3:
						print(neighbours, 'fish')
						new_field[i][j] = fish
					elif neighbours.count(shrimp) == 3:
						print(neighbours, 'shrimp')
						new_field[i][j] = shrimp
					else:
						new_field[i][j] = field[i][j]
	return new_field







def main():
	'''
	Главная функция программы
	'''
	n = int(input("Введите высоту поля: "))
	while n <= 0:
		n = int(input("Пожалуйста, введите еще раз высоту: "))
	m = int(input("Введите ширину поля: "))
	while n <= 0:
		n = int(input("Пожалуйста, введите еще раз высоту: "))

	mode = int(input("Введите тип игры. 1 - пошаговая, 2 - поле все время отрисовывается: "))
	while mode != 1 and mode != 2:
		mode = int(input("Пожалуйста, введите еще раз: "))

	field = field_gen(n, m)
	while True:
		field_draw(field, mode)
		if mode == 1:
			print("Нажмите любую клавишу для продолжения")
			input()
		field = move(field, n, m)









if __name__ == "__main__":
	main()
