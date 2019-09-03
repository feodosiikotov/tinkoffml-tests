from numpy import random
import re
import pickle

def prepare_text(text):
	'''
	Функция подготовки текста к обработке
	Приводит все слова к нижнему регистру, удаляет все лишние знаки
	'''
	text = text.lower()
	words = re.split('[^а-я]', text)
	words = list(filter(None, words))
	return words

def output(mode='console', file=None):
	'''
	Функция вывода текста в файл или консоль, в зависимости от выбранного режима
	'''
	if mode == 'console':
		return print
	elif mode == 'file':
		return file.write
	else:
		raise AttributeError


class TextGenerator:
	'''
	Генератор текста на основе биграммной языковой модели
	'''
	def __init__(self):
		self.word_frequency = {}
		self.pairs_frequency = {}

	def fit(self, words):
		'''
		Обучение. Считается вероятность каждого слова, а также вероятность пары слов
		'''
		words_len = len(words)
		self.word_frequency = {word: words.count(word)/words_len for word in set(words)}
		for i in range(words_len - 1):
			if words[i] not in self.pairs_frequency:
				self.pairs_frequency[words[i]] = {words[i + 1]: 1/(self.word_frequency[words[i]]*words_len)}
			else:
				if words[i + 1] in self.pairs_frequency[words[i]]:
					self.pairs_frequency[words[i]][words[i + 1]] += 1/(self.word_frequency[words[i]]*words_len)
				else:
					self.pairs_frequency[words[i]][words[i + 1]] = 1/(self.word_frequency[words[i]]*words_len)
		self.pairs_frequency[words[words_len - 1]] = None

	def generate(self, amount_of_words, mode='console', file=None):
		'''
		Генерация текста на основе вероятности каждой пары и слова
		'''
		outputf = output(mode, file)
		start_word = random.choice(list(self.word_frequency), p=list(self.word_frequency.values()))
		outputf(start_word + ' ')
		prev_word = start_word
		for i in range(amount_of_words - 1):
			if self.pairs_frequency[prev_word] == None:
				return
			next_word = random.choice(list(self.pairs_frequency[prev_word]), p=list(self.pairs_frequency[prev_word].values()))
			outputf(next_word + ' ')
			prev_word = next_word

	def save_model(self, filename):
		'''
		Сохранить модель в файл
		'''
		with open(filename, 'wb') as f:
			pickle.dump(self, f)

		



def main():
	filename = input("Введите имя файла с текстами для обучения: ")
	try:
		with open(filename, 'r') as f:
			text = f.read()
	except:
		print("Неверное имя файла")
		exit()
	words = prepare_text(text)
	model = TextGenerator()
	model.fit(words)
	model.generate(100, mode='file', filename='123.txt')



if __name__ == "__main__":
	main()