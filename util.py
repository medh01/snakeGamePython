import pygame as pg
from random import *
pg.init()
sound = pg.mixer.Sound("snakeEatingSound.mp3")

class Head : 
	def __init__(self):
		self.x=randint(1,700)
		self.y=randint(1,500)
		self.vel=16
		self.direction = "right"
		
	
	def move(self):
		if self.direction == "right" :
			if self.x <768 :
				self.x+=self.vel				
			else:
				self.x=0
			
		if self.direction == "left" :
			if self.x >0 :
				self.x-=self.vel
			else:
				self.x = 0
	
		if self.direction == "top" :
			if self.y > 0 :
				self.y-=self.vel
			else:
				self.y = 0
	
		if self.direction == "bottom" :
			if self.y < 568 :
				self.y+=self.vel
			else:
				self.y = 0
									 				
class Snake: 
	def __init__(self,head):
		self.head=head
		self.tail=[(self.head.x,self.head.y)]
		self.nbFruitEaten=0
	
	def growTail(self,headRect,foodRect,food):
		if headRect.colliderect(foodRect):
			if self.head.direction == "right" :
				self.head.x+=16
			elif self.head.direction == "left" :
				self.head.x-=16
			elif self.head.direction == "top" :
				self.head.y-=16
			else:
				self.head.y+=16
			self.tail.insert(0,(self.head.x,self.head.y))
			food.gotEaten()
			self.nbFruitEaten+=1
			pg.mixer.Sound.play(sound)
	
	def move(self):
		self.head.move()
		self.tail.insert(0,(self.head.x,self.head.y))
		del(self.tail[-1])
	
	def gotBiten(self,headRect,l):
		for item in l :
			if headRect.colliderect(item) :
				return True
		return False 	

class Food: 
	def __init__(self):
		self.x = randint(100,700) 
		self.y = randint(100,500)
	
	def gotEaten(self):
		self.x = randint(100,700) 
		self.y = randint(100,500)
