import pygame as pg
from random import *

pg.init()

screen = pg.display.set_mode((800,600))

pg.display.set_caption("snake game")
class BodyPart :
	def __init__(self,x,y):  
		self.x=x
		self.y=y
		self.vel=5
		self.lastX=x
		self.lastY=y
	
	
		
	
class Head (BodyPart): 
	def __init__(self):
		BodyPart.__init__(self,randint(1,700),randint(1,500))
		self.direction = "right" 
	
	def move(self):
		if self.direction == "right" :
			self.lastX = self.x
			if self.x <768 :
				self.x+=self.vel
				
			else:
				self.x=0
			
		if self.direction == "left" :
			self.lastX = self.x
			if self.x >0 :
				self.x-=self.vel
			else:
				self.x=768
	
		if self.direction == "top" :
			self.lastY = self.y
			if self.y > 0 :
				self.y-=self.vel
			else:
				self.y = 568
	
		if self.direction == "bottom" :
			self.lastY = self.y
			if self.y < 568 :
				self.y+=self.vel
			else:
				self.y=0
	
		
class TailPart (BodyPart):
	def __init__(self,x,y) :
		BodyPart.__init__(self,x,y)
		

				 		
		
class Snake: 
	def __init__(self,head):
		self.head=head
		self.tail=[]
	
	def growTail(self):
		if len(self.tail) :
			lastTailPart = self.tail[-1] 
			self.tail.append(TailPart(lastTailPart.lastX,lastTailPart.lastY))
		else :
			self.tail.append(TailPart(self.head.lastX,self.head.lastY))
	
	def moveTail(self):
		if self.head.direction in ["right","left"] :
			self.tail[0].x=self.head.lastX
			self.tail[0].y=self.head.lastY
		else:
			self.tail[0].x=self.head.lastX
			self.tail[0].y=self.head.lastY-32
			
	
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
	if  (i==5):
		snake.growTail()			
		pg.draw.rect(screen,(255,0,0),(snake.tail[0].x,snake.tail[0].y,32,32))
	if i>5 :
		snake.moveTail()
		pg.draw.rect(screen,(0,255,0),(snake.tail[0].x,snake.tail[0].y,32,32))
	pg.display.update()


