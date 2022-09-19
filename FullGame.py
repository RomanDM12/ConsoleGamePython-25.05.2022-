#!/bin/usr/env python 3

import sys
import time
from os import system

cnt = 0
class Scene:
	map1 = [
	        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
	        ["#", " ", " ", " ", " ", " ", "#", "@", "@", "@", "@", "@", " ", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", " ", " ", " ", "#", "Б", "у", "ф", "е", "т", " ", " ", " ", " ", "+", " ", " ", "#"],
	        ["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "!"],
	        ["#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", "#", "#", "#", "#", "#", "-", "-", "#", "#", "-", "-", "#", "#", "#", "#", "#"],
	        ["#", " ", " ", " ", " ", " ", "P", "#", " ", "T", "o", "i", "l", "e", "t", " ", "#", " ", " ", "#"],
	        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
	map2 = [
	        ["#", "#", "#", "!", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
	        ["#", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", "#", "P", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", "#", "#", " ", " ", " ", " ", " ", "#", "#", "#", "#", "#", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", "+", " ", "#", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", "#", "#", "#", " ", " ", " ", " ", " ", "#", "#", "#", "-", "#", "-", "#", "#"],
	        ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "T", "o", "i", "l", "e", "t", "#"],
	        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
	map3 = [
	        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
	        ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
	        ["#", " ", " ", "#", "P", " ", "#", " ", " ", " ", "#", "#", "#", "#", " ", " ", " ", " ", "@", "#"],
	        ["#", " ", " ", "#", "#", "#", "#", " ", " ", "#", "К", "а", "ф", ".", "#", " ", " ", "+", "@", "#"],
	        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", "О", "х", "р", "а", "#", " ", " ", " ", "@", "#"],
	        ["#", " ", " ", " ", " ", " ", " ", " ", " ", "#", " ", "н", "ы", " ", "#", " ", " ", " ", " ", "#"],
	        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "!", "#", "#", "#"]]

#	map1 = open("map_0_1.txt", "r")
#	map2 = open("map_0_2.txt", "r")
#	def loadMap(self, map):
#		for row in map:
#			read_row = row.strip()
#			m.append(read_row)

	def mapShow(self, map):
		map[self.x][self.y] = "P"
		system("clear")
		for row in map:
			print("")
			for i in row:
				print(i, end=' ')

class Engine(Scene):

	def playerPos(self, map):
		x = -1
		y = 0
		for i in map:
			x += 1
			for j in i:
				if j == "P":
					self.x = x
					self.y = y
				else:
					y += 1
			y = 0

	legalCheat = False
	def movement(self, map, cnt):
		print("\nHomo: Вы находитесь рядом с аудиторией.")
		print("Homo: Вам нужно дойти до аудитории, в которой проводится экзамен.")
		print("Homo: Поторопитесь, он вот-вот начнется!")
		print("'!' - аудитория, где сдается экзамен")
		print("'+' - подсказка, которую вы можете получить у одногруппника")
		print("'P' - студент")
		print("Перемещение с помощью клавиш(w-вверх, a-влево, s-вниз, d-вправо)\n")

		move = input(">")
		if move == "a": #влево
			map[self.x][self.y] = " "
			if map[self.x][self.y-1] == "+":
				self.legalCheat = True
			if map[self.x][self.y-1] == "!":
				self.perenapr(cnt)
			if  map[self.x][self.y-1] != "#" and map[self.x][self.y-1] != "@" and map[self.x][self.y-1] != "-":
				self.y -= 1
		if move == "w": #вверх
			map[self.x][self.y] = " "
			if map[self.x-1][self.y] == "+":
				self.legalCheat = True
			if map[self.x-1][self.y] == "!":
				self.perenapr(cnt)
			if map[self.x-1][self.y] != "#" and map[self.x-1][self.y] != "@" and map[self.x-1][self.y] != "-":
				self.x -= 1
		if move == "d": #вправо
			map[self.x][self.y] == " "
			if map[self.x][self.y+1] == "+":
				self.legalCheat = True
			if map[self.x][self.y+1] == "!":
				self.perenapr(cnt)
			if map[self.x][self.y+1] != "#" and map[self.x][self.y+1] != "@" and map[self.x][self.y+1] != "-":
				self.y += 1
				map[self.x][self.y - 1] = " "
		if move == "s": #вниз
			map[self.x][self.y] == " "
			if map[self.x+1][self.y] == "+":
				self.legalCheat = True
			if map[self.x+1][self.y] == "!":
				self.perenapr(cnt)
			if map[self.x+1][self.y] != "#" and map[self.x+1][self.y] != "@" and map[self.x+1][self.y] != "-":
				self.x += 1
				map[self.x - 1][self.y] = " "

class Tasks(Engine):

	def printReplicas(self, text):
		for i in text:
			sys.stdout.write(i)
			sys.stdout.flush()
			time.sleep(0.02)
		time.sleep(0.1)

	def startTask(self, cnt, timesmat, timesprog, timesond):

		a = timesmat  #флаг для каждого предмета
		b = timesprog #чтобы каждый предмет был сдан один раз
		c = timesond
		cnt += 1

		if cnt == 1:
			Tasks.printReplicas(0, "Homo: Привет студент!\n")
			Tasks.printReplicas(0, "Homo: Твоя задача успешно сдать сессию!\n")
			Tasks.printReplicas(0, "Homo: Впереди тебе предстоит преодолеть три экзамена\n")
			Tasks.printReplicas(0, "Homo: Три верных ответа гарантируют успешную сдачу сессии\n")
			Tasks.printReplicas(0, "Homo: Желаю удачи в прохождении! +_+\n")
			print("""        ______________________________________________________________________
                         _____|____     _____|____     _____|____
			/   Матан  \   /   Прога  \   /    ОНД   \ \n                        \----------/   \----------/   \----------/
			""")
			Tasks.printReplicas(0, "Какой из экзаменов будешь сдавать первым?\n")

		if cnt == 3:
			Tasks.printReplicas(0, "Выберите следующий экзамен\n")
		if cnt == 5:
			Tasks.printReplicas(0, "Выберите последний экзамен\n")
		if cnt == 7:
			print("--------------------------------------------------------------")
			Tasks.printReplicas(0, "Ура!\n")
			Tasks.printReplicas(0, "Ты получил три правильных ответа\n")
			self.success()

		while True:
			choice = input("> ").lower()
			if choice == "матан" and a != True:
				self.firstTask("матан", cnt)
			if choice == "прога" and b != True:
				self.secondTask("прога", cnt)
			if choice == "онд" and c != True:
				self.thirdTask("онд", cnt)
			else:
				print("Такого экзамена не существует или вы его уже прошли")
#перемещение на карты
	def firstTask(self, subject, cnt):
		self.subject = subject
		self.playerPos(self.map1)
		self.legalCheat = False
		while True:
			self.mapShow(self.map1)
			self.movement(self.map1, cnt)
	def secondTask(self, subject, cnt):
		self.subject = subject
		self.playerPos(self.map2)
		self.legalCheat = False
		while True:
			self.mapShow(self.map2)
			self.movement(self.map2, cnt)
	def thirdTask(self, subject, cnt):
		self.subject = subject
		self.playerPos(self.map3)
		self.legalCheat = False
		while True:
			self.mapShow(self.map3)
			self.movement(self.map3, cnt)

	def keys(self, cnt): #функция без подсказок(legalCheat=False)
		if self.subject == "матан":
			timesmat = True
			kol = 0
			print("Следует решить данное уравнение: 6x + 72 = 0")
			while kol != 4:
				answer = input("> ")
				if answer == '-12':
						cnt += 1
						print("Верно!")
						Tasks.startTask(self, cnt, timesmat, 0, 0)
				else:
					print("У тебя осталось попыток: ", 2 - kol)
					kol += 1
					if kol == 3:
						self.fail("Ты не смог сдать один из предметов")
						exit(0)
		if self.subject == "прога":
			timesprog = True
			kol = 0
			print("Функция в си, используемая для динамического выделения памяти?")
			while kol != 3:
				answer = input("> ")
				if answer == 'malloc':
						cnt += 1
						print("Верно!")
						Tasks.startTask(self, cnt, 0, timesprog, 0)
				else:
					print("У тебя осталось попыток: ", 2 - kol)
					kol += 1
					if kol == 3:
						self.fail("Ты не смог сдать один из предметов")
						exit(0)
			self.fail("Ты не смог сдать один из предметов")
		if self.subject == "онд":
			timesond = True
			kol = 0
			print("Написать равенство коммутативности по сложению для переменных a и b")
			while kol != 3:
				answer = input("> ")
				if answer == "a+b=b+a":
						cnt += 1
						print("Верно!")
						Tasks.startTask(self, cnt, 0, 0, timesond)
				else:
					print("У тебя осталось попыток: ", 2 - kol)
					kol += 1
					if kol == 3:
						self.fail("Ты не смог сдать один из предметов")
						exit(0)

	def cheatKeys(self, cnt): #функция с подсказками(legalCheat=True)
		kol = 0
		if self.subject == "матан":
			timesmat = True
			print("Следует решить данное уравнение: 6x + 72 = 0")
			print("** Подсказка: ответом является отрицательное число **")
			while kol != 3:
				answer = input("> ")
				if answer == '-12':
					cnt += 1
					print("Верно!")
					Tasks.startTask(self, cnt, timesmat, 0, 0)
				else:
					print("У тебя осталось попыток: ", 2 - kol)
					kol += 1
					if kol == 3:
						self.fail("Ты не смог сдать один из предметов")
						exit(0)
		if self.subject == "прога":
			timesprog = True
			kol = 0
			print("Функция в си, используемая для динамического выделения памяти?")
			print("** Подсказка: Данная функция берется из библиотеки stdlib.h **")
			while kol != 3:
				answer = input("> ")
				if answer == 'malloc':
					cnt += 1
					print("Верно!")
					Tasks.startTask(self, cnt, 0, timesprog, 0)
				else:
					print("У тебя осталось попыток: ", 2 - kol)
					kol += 1
					if kol == 3:
						self.fail("Ты не смог сдать один из предметов")
						exit(0)
		if self.subject == "онд":
			timesond = True
			kol = 0
			print("Написать равенство коммутативности по сложению для переменных a и b")
			print("** Подсказка: от перемены мест слагаемых сумма не меняется **")
			while kol != 3:
				answer = input("> ")
				if answer == "a+b=b+a":
					cnt += 1
					print("Верно!")
					Tasks.startTask(self, cnt, 0, 0, timesond)
				else:
					print("У тебя осталось попыток: ", 2 - kol)
					kol += 1
					if kol == 3:
						self.fail("Ты не смог сдать один из предметов")
						exit(0)
class Game(Tasks):

	def preview(self):
		Tasks.printReplicas(0, "Game: TOP EXAMS\n")
		Tasks.printReplicas(0, "Present by ConliR Games\n")
		Tasks.printReplicas(0, "Приветствую! Данная игра представляет собой симулятор сдачи сессии!\n")
		print("-----------------------------------------------------------------------")

	def play(self):
		system("clear")
		self.preview()
		self.startTask(cnt, 0, 0, 0)

	def fail(self, ok):
		print("У тебя не получилось сдать сессию на отлично. ;(")
		print("В следующий раз обязательно получится!")

	def perenapr(self, cnt):

		if self.legalCheat == True:
			self.cheatKeys(cnt)
		else:
			self.keys(cnt)

	def success(self):
		Tasks.printReplicas(self, "Ты справился со сдачей всех экзаменов на отлично!!!\n")
		Tasks.printReplicas(self, "Спасибо за прохождение моей игры!\n")
		Tasks.printReplicas(self, "Разработал: Дмитриев Роман  Группа: ККСО-04-21\n")
		print("------------------------------------------------------------------------")
		exit(0)

alpha = Game()
alpha.play()

#Дмитриев Роман ККСО-04-21
