import pygame as pg
from util import * 

pg.init()
screen = pg.display.set_mode((800,600))

#fonts
pg.display.set_caption("snake game")
font = pg.font.Font(None,30)

#background music
pg.mixer.music.load("sounds/bg.mp3")
pg.mixer.music.play(-1)

#game loop

running = True 
head = Head()
snake = Snake(head)
food = Food()
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
			headRect = pg.draw.rect(screen,(24,29,39),(snake.tail[i][0],snake.tail[i][1],20,20))
		else:
			if i%2 :
				partRect = pg.draw.rect(screen,(37,77,50),(snake.tail[i][0],snake.tail[i][1],20,20))
			else:
				partRect = pg.draw.rect(screen,(24,29,39),(snake.tail[i][0],snake.tail[i][1],20,20))
		
	foodRect = pg.draw.rect(screen,(153,15,2),(food.x,food.y,16,16))
	snake.growTail(headRect,foodRect,food)
	text = font.render(f"score : {snake.nbFruitEaten}", True, (0,0,0))
	screen.blit(text,(10,10))
	pg.display.update()


