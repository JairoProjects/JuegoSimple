import pygame
import random
import math
pi = math.pi

#Defining colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
MAGENTA = (255,0,255)
CIAN = (0,255,255)
YELLOW = (255,255,0)
ORANGE = (255,153,0)

#Defining classes

class Enemy(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()
		self.image = pygame.Surface([5, 7])
		self.image.fill(color)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.x -= 5
		if self.rect.x<=0:
			self.rect.x=700

class Player(pygame.sprite.Sprite):
	speedX=0
	def __init__(self, color):
		super().__init__()
		self.image = pygame.Surface([5, 7])
		self.image.fill(AMARILLO)
		self.rect = self.image.get_rect()
	def updateRight(self):
                Player.speedX+=1
		self.rect.x+=Player.speedX
                playSound("step.ogg")
	def updateLeft(self):
                Player.speddX-=1
		self.rect.x+=Player.speedX
                playSound("step.ogg")
	def stop(self):
		self.rect.x=self.rect.x

class Bullet(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()
		self.image = pygame.Surface([3, 1])
		self.image.fill(AZUL)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.x+=6

pygame.init()
dimensions = (700,500)
screen = pygame.display.set_mode(dimensions)
pygame.mixer.music.load("music.ogg")
pygame.mixer.music.play(-1, 0.0)

pygame.display.set_caption("Juego")

def playSound(sound):
	#Reproduce un sonido, que tiene que estar en la misma carpeta que el archivo
	played = pygame.mixer.Sound(sound)
	played.play()

enemiesList=pygame.sprite.Group()
spritesList=pygame.sprite.Group()
bulletsList=pygame.sprite.Group()
enemiesHitList=[]

for x in range(50):
	enemy=Enemy(GREEN)
	enemy.rect.x=random.randint(350, 700)
	enemy.rect.y=490
	enemiesList.add(enemy)
	spritesList.add(enemy)

player=Player(YELLOW)
player.rect.x=0
player.rect.y=490
spritesList.add(player)

end=False
timer=pygame.time.Clock()
while not end:
	for event in pygame.event.get():
		if event.type == pygame.quit:
			end=true
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				player.updateLeft()
			if event.type == pygame.K_RIGHT:
				player.updateRight()
			if event.type == pygame.K_SPACE:
				bullet=Bullet(RED)
				bullet.rect.x=player.rect.x
				bullet.rect.y=player.rect.y
				spritesList.add(bullet)
				bulletsList.add(bullet)
				playSound("shoot.ogg")
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				player.stop()
			if event.type == pygame.K_RIGHT:
				player.stop()

		spritesList.update()
		for bullet in bulletsList:
			enemiesHitList=pygame.sprite.spritecollide(bullet, enemiesList, True)
		for enemy in enemiesHitList:
			bulletsList.remove(bullet)
			spritesList.remove(bullet)
			enemiesList.remove(enemy)
			spritesList.remove(enemy)


	screen.fill(WHITE)
	spritesList.draw(screen)
	pygame.display.flip()
	timer.tick(60)

pygame.quit
