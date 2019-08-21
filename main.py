# -*- conding:utf-8 -*-

import os
import time

from random import randrange

def main():
	tries = 10
	score = 0

	print('Bienvenue au jeu d\'entrainement à l\'écriture au clavier.\n')
	print('Saisisez ces mots en moins de 5 secondes.\n')

	print('Appuez sur "Entrée" pour continuer...')
	input()

	for i in range(tries):
		word = get_rand_word('mots.txt')

		print('Saisisez ce mot: ', word)
		started_time = time.time()

		user_word = str(input())

		time_elapsed = round(time.time() - started_time)

		if time_elapsed <= 5 and user_word.capitalize() == word:
			score += 1

			print('\nBravo vous l\'avez saisie rapidement !\n')

		elif time_elapsed > 5:
			print('\nTrop lent !\n')

		if user_word.capitalize() != word:
			print('Vous avez mal ecrit le mot\n')

	print('Terminé ! Votre score {}/{}'.format(score, tries))


def get_rand_word(path_to_file):
	file = open(path_to_file, 'r')
	indexes = []

	words = [word for word in file.read().split('\n')]

	while True:
		rand_index = randrange(len(words))

		if rand_index in indexes:
			continue
		else:
			break

	indexes.append(rand_index)
	word = words[rand_index]

	file.close()

	return word.capitalize()


if __name__ == '__main__':
	main()
