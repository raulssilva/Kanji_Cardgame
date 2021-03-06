import pygame
from settingsMenu import *
from karutaGame import *
from portugueseGame import *
from japaneseGame import *

class Play:
	def __init__(self, screen, settingsMenu):
		self.screen = screen
		self.surface = pygame.Surface((795, 411))
		self.settingsMenu = settingsMenu

		self.currtentItem = 1

		self.fontPlay = pygame.font.Font("./Fonts/Kengo.ttf", 62)
		self.fontItens = pygame.font.SysFont("monospace", 25)

		self.playName = self.fontPlay.render("Play", 1, (255,69,0))
		self.karutaName = self.fontItens.render("Karuta", 1, (0,100,0))
		self.portugueseName = self.fontItens.render("Portuguese", 1, (255,255,255))
		self.japaneseName = self.fontItens.render("Japanese", 1, (255,255,255))
		self.backName = self.fontItens.render("Back", 1, (255,255,255))

	def playSound(self, idSound):
		sound = pygame.mixer.Sound("./Sounds/Karuta.wav")
		if idSound == 1:
			sound = pygame.mixer.Sound("./Sounds/Karuta.wav")
		elif idSound == 2:
			sound = pygame.mixer.Sound("./Sounds/Portuguese.wav")
		elif idSound == 3:
			sound = pygame.mixer.Sound("./Sounds/Japanese.wav")
		elif idSound == 4:
			sound = pygame.mixer.Sound("./Sounds/Back.wav")

		sound.set_volume(0.8)
		pygame.mixer.Sound.play(sound)

	def draw(self):
		self.surface.fill((0,0,0))
		self.screen.blit(self.surface, [0,0])

		self.screen.blit(self.playName, (325, 50))
		self.screen.blit(self.karutaName, (30, 200))
		self.screen.blit(self.portugueseName, (30, 230))
		self.screen.blit(self.japaneseName, (30, 260))
		self.screen.blit(self.backName, (700, 350))

	def itemUp(self):
		if self.currtentItem == 1:
			pass
		else:
			self.currtentItem -= 1;
			self.karutaName = self.fontItens.render("Karuta", 1, (255,255,255))
			self.portugueseName = self.fontItens.render("Portuguese", 1, (255,255,255))
			self.japaneseName = self.fontItens.render("Japanese", 1, (255,255,255))
			self.backName = self.fontItens.render("Back", 1, (255,255,255))

			if self.currtentItem == 1:
				self.karutaName = self.fontItens.render("Karuta", 1, (0,100,0))
			elif self.currtentItem == 2:
				self.portugueseName = self.fontItens.render("Portuguese", 1, (0,100,0))
			elif self.currtentItem == 3:
				self.japaneseName = self.fontItens.render("Japanese", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.backName = self.fontItens.render("Back", 1, (0,100,0))

			self.draw()
			self.playSound(self.currtentItem)

	def itemDown(self):
		if self.currtentItem == 4:
			pass
		else:
			self.currtentItem += 1;
			self.karutaName = self.fontItens.render("Karuta", 1, (255,255,255))
			self.portugueseName = self.fontItens.render("Portuguese", 1, (255,255,255))
			self.japaneseName = self.fontItens.render("Japanese", 1, (255,255,255))
			self.backName = self.fontItens.render("Back", 1, (255,255,255))

			if self.currtentItem == 1:
				self.karutaName = self.fontItens.render("Karuta", 1, (0,100,0))
			elif self.currtentItem == 2:
				self.portugueseName = self.fontItens.render("Portuguese", 1, (0,100,0))
			elif self.currtentItem == 3:
				self.japaneseName = self.fontItens.render("Japanese", 1, (0,100,0))
			elif self.currtentItem == 4:
				self.backName = self.fontItens.render("Back", 1, (0,100,0))

			self.draw()
			self.playSound(self.currtentItem)

	def selectItem(self):
		karuta = Karuta(self.screen, self.settingsMenu)
		portuguese = Portuguese(self.screen, self.settingsMenu)
		japanese = Japanese(self.screen, self.settingsMenu)

		if self.currtentItem == 1:
			karuta.start()
			self.draw()
		elif self.currtentItem == 2:
			portuguese.start()
			self.draw()
		elif self.currtentItem == 3:
			japanese.start()
			self.draw()
		elif self.currtentItem == 4:
			return True