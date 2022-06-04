#imports 
import pygame as pg
from modules.classes import * 

pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("snake game")

#loading fonts
f25 = pg.font.Font('fonts/Oswald-RegularItalic.ttf',25)
f50 = pg.font.SysFont('fonts/Oswald-RegularItalic.ttf',50)

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
	screen.fill((128,128,128))    #grey color 
	for event in pg.event.get() :
		if event.type == pg.QUIT:
			running = False
		
	#keys control
	#the snake can't move in the opposite direction
	#for example if the snake is moving to the right it can't move the left directly 
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

	#drawing the snake and the food
	tailParts=[] 
	for i in range(len(snake.tail)):
		if i == 0 : 
			headRect = pg.draw.rect(screen,(24,29,39),(snake.tail[i][0],snake.tail[i][1],20,20))
		else:
			if i%2 :
				tailPart = pg.draw.rect(screen,(37,77,50),(snake.tail[i][0],snake.tail[i][1],20,20))
				tailParts.append(tailPart)
			else:
				tailPart = pg.draw.rect(screen,(24,29,39),(snake.tail[i][0],snake.tail[i][1],20,20))
				tailParts.append(tailPart)
	
	foodRect = pg.draw.rect(screen,(153,15,2),(food.x,food.y,16,16))
	
	#detect if the snake had bitten itself
	for tailPart in tailParts:
		if headRect.colliderect(tailPart):
			snake.head.gameOver = True

	snake.growTail(headRect,foodRect,food)
	
	#printing the score on screen
	text = f25.render(f"score : {snake.nbFruitEaten}", True, (0,0,0))
	screen.blit(text,(10,10))
	
	pg.display.update()
	
	#the gameover handling 
	if snake.head.gameOver :
		pg.mixer.music.pause()
		sound= pg.mixer.Sound("sounds/gameOverSound.wav")
		pg.mixer.Sound.play(sound)
	
	while snake.head.gameOver :
		screen.fill((128,128,128)) #grey color
		gameOverText = f50.render("game over", True, (153,15,2)) #red color
		instructionsText = f25.render("press space to play again or press q to exit", True, (0,0,0))
		screen.blit(gameOverText,(400-gameOverText.get_width()//2,300-gameOverText.get_height()//2))
		screen.blit(instructionsText,(400-instructionsText.get_width()//2,300-instructionsText.get_height()//2+gameOverText.get_height()))
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE :
					snake.head.gameOver = False
					head = Head()
					snake = Snake(head)
					food = Food()
					pg.mixer.music.play(-1)
				if event.key == pg.K_q :
					snake.head.gameOver = False
					running = False
		pg.display.update()


