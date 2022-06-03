import pygame as pg
from random import *

pg.init()

screen = pg.display.set_mode((800,600))

pg.display.set_caption("snake game")


#game components			
class Head : 
	def __init__(self):
		self.x=randint(1,700)
		self.y=randint(1,500)
		self.vel=32
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
				self.x=768
	
		if self.direction == "top" :
			if self.y > 0 :
				self.y-=self.vel
			else:
				self.y = 568
	
		if self.direction == "bottom" :
			if self.y < 568 :
				self.y+=self.vel
			else:
				self.y=0
									 				
class Snake: 
	def __init__(self,head):
		self.head=head
		self.tail=[(self.head.x,self.head.y)]
	
	def growTail(self,headRect,foodRect,food):
		if headRect.colliderect(foodRect):
			if self.head.direction == "right" :
				self.head.x+=32
			elif self.head.direction == "left" :
				self.head.x-=32
			elif self.head.direction == "top" :
				self.head.y-=32
			else:
				self.head.y+=32
			self.tail.insert(0,(self.head.x,self.head.y))
			food.gotEaten()
	
	def move(self):
		self.head.move()
		self.tail.insert(0,(self.head.x,self.head.y))
		del(self.tail[-1])				

class Food: 
	def __init__(self):
		self.x = randint(1,700) 
		self.y = randint(1,500)
	
	def gotEaten(self):
		self.x = randint(1,700) 
		self.y = randint(1,500)
			
				


#game loop
head = Head()
snake = Snake(head)
food = Food() 
running = True 

while running : 
	pg.time.delay(120)
	screen.fill((128,128,128)) 
	for event in pg.event.get() :
		if event.type == pg.QUIT:
			running = False
	
	#keys control
	keys = pg.key.get_pressed()
	if keys[pg.K_UP] :
		if snake.head.direction != "bottom": 
			snake.head.direction = "top"
	
	if keys[pg.K_DOWN] :
		if snake.head.direction != "top":
			snake.head.direction = "bottom"
	
	if keys[pg.K_LEFT] :
		if snake.head.direction != "right":
			snake.head.direction = "left"
	
	if keys[pg.K_RIGHT] :
		if snake.head.direction != "left":
			snake.head.direction = "right" 

	
	snake.move()
	#drawing the snake
	for i in range(len(snake.tail)):
		if i == 0 : 
			headRect = pg.draw.rect(screen,(24,29,39),(snake.tail[i][0],snake.tail[i][1],32,32))
		else:
			if i%2 :
		 		pg.draw.rect(screen,(37,77,50),(snake.tail[i][0],snake.tail[i][1],32,32))
			else:
				pg.draw.rect(screen,(24,29,39),(snake.tail[i][0],snake.tail[i][1],32,32))
	
	foodRect = pg.draw.rect(screen,(153,15,2),(food.x,food.y,16,16))
	snake.growTail(headRect,foodRect,food)
	pg.display.update()


