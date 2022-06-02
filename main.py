import pygame as pg
from random import *

pg.init()

screen = pg.display.set_mode((800,600))

pg.display.set_caption("snake game")
class BodyPart :
	def __init__(self,x,y,direction):  
		self.x=x
		self.y=y
		self.direction = direction
		self.vel=5
	
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
		
	
class Head (BodyPart): 
	def __init__(self):
		BodyPart.__init__(self,randint(1,700),randint(1,500),"right") 
		
class TailPart (BodyPart):
	def __init__(self,x,y,direction) :
		BodyPart.__init__(self,x,y,direction)
		
		
class Snake: 
	def __init__(self,head):
		self.head=head
		self.tail=[]
	
	def growTail(self):
		if len(self.tail) :
			lastTailPart = self.tail[-1] 
			self.tail.append(TailPart(lastTailPart.x,lastTailPart.y,lastTailPart.direction))
		else :
			self.tail.append(TailPart(self.head.x,self.head.y,self.head.direction))

head = Head()
snake = Snake(head)



running = True 
i=0
while running : 
	pg.time.delay(100)
	i+=1
	screen.fill((0,0,0)) 
	for event in pg.event.get() :
		if event.type == pg.QUIT:
			running = False
	
	#moving the head
	keys = pg.key.get_pressed()
	if keys[pg.K_UP] :
		snake.head.direction = "top"
	
	if keys[pg.K_DOWN] :
		snake.head.direction = "bottom"
	
	if keys[pg.K_LEFT] :
		snake.head.direction = "left"
	
	if keys[pg.K_RIGHT] :
		snake.head.direction = "right" 

	
	snake.head.move()
	pg.draw.rect(screen,(255,0,0),(snake.head.x,snake.head.y,32,32))
	if not (i%5):
		snake.growTail()
		snake.tail[0].move()	
		pg.draw.rect(screen,(255,0,0),(snake.tail[0].x,snake.tail[0].y,32,32))
	pg.display.update()


