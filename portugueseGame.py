import pygame
import time
from threading import Thread
from settingsMenu import *

counter = 5
lifes = 3

class Timer(Thread):
	def __init__(self, num, screen):
		Thread.__init__(self)
		self.num = num
		self.screen = screen
		self.surface = pygame.Surface((795, 411))

		self.fontDescription = pygame.font.SysFont("monospace", 25)

	def run(self):
		global counter
		while counter >= 0:
			self.draw()
			time.sleep(1)
			counter -= 1


	def draw(self):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])
		
		self.heart = pygame.image.load('./Images/heart.png')
		self.kanjiName = self.fontDescription.render("AMOR", 1, (255,255,255))
		self.screen.blit(self.kanjiName, (360, 150))

		self.secondsName = self.fontDescription.render(str(counter) + "s", 1, (255,255,255))
		self.screen.blit(self.secondsName, (375, 300))

		global lifes
		if lifes == 1:
			self.screen.blit(self.heart, (725, 20))
		elif lifes == 2:
			self.screen.blit(self.heart, (725, 20))
			self.screen.blit(self.heart, (680, 20))
		elif lifes == 3:
			self.screen.blit(self.heart, (725, 20))
			self.screen.blit(self.heart, (680, 20))
			self.screen.blit(self.heart, (635, 20))
		
		pygame.display.flip()
		

class Portuguese:
	def __init__(self, screen, settingsMenu):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))
		self.settingsMenu = settingsMenu

		self.fontPortuguese = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontDescription = pygame.font.SysFont("monospace", 25)

		global counter
		counter = self.settingsMenu.timeValue

	def start(self):
		self.portugueseName = self.fontPortuguese.render("Portuguese", 1, (255,69,0))
		self.descriptionName = self.fontDescription.render("The game will ask for the kanjis, in portuguese", 1, (255,255,255))

		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.portugueseName, (215, 100))
		self.screen.blit(self.descriptionName, (40, 200))
		pygame.display.flip()
		time.sleep(3)
		self.play()

	def play(self):
		countDown = Timer(1, self.screen)
		countDown.start()

		countDown.join()

		global lifes
		global counter
		if counter <= 0:
			lifes -= 1
			if lifes > 0:
				counter = self.settingsMenu.timeValue
				self.play()
			if lifes == 0:
				self.gameOver = self.fontPortuguese.render("Game Over", 1, (255,0,0))

				self.surface.fill((0,0,0))
				self.screen.blit(self.surface, [0,0])

				self.screen.blit(self.gameOver, (250, 175))
				pygame.display.flip()
				time.sleep(1)
				lifes = 3