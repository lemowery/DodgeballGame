import pygame
import time
import random

pygame.init()

# Set display height and width
display_width = 900
display_height = 900

# Define colors
brown = (170, 89, 1)
white = (255, 255, 255)
red = (155, 0, 0)

person_width = 73

# Set game display size
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Change window name
pygame.display.set_caption('Dodgeball')

# Define game clock
clock = pygame.time.Clock()

charImg = pygame.image.load('character.png')
background = pygame.image.load('gymfloor.png')
ballImg = pygame.image.load('ball.png')

def score_count(count):
	displayText = pygame.font.Font("Consolas.ttf", 75)
	displayText = displayText.render(str(count), True, white)
	gameDisplay.blit(displayText, (display_width / 2, 50))

def text_objects(text, font):
	textSurface = font.render(text, True, red)
	return textSurface, textSurface.get_rect()

def show_message(text):
	displayText = pygame.font.Font("Consolas.ttf", 75)
	displayText.set_bold(True)
	textSurface, textRectangle = text_objects(text, displayText)
	textRectangle.center = ((display_width * 0.5), (display_height * 0.3))
	gameDisplay.blit(textSurface, textRectangle)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def hit():
	show_message("YOU GOT DRILLED!")

def ball(ball_startx, ball_starty):
	gameDisplay.blit(ballImg, (ball_startx, ball_starty))

def char(x, y):
	gameDisplay.blit(charImg, (x, y))

def game_loop():

	# Set character position and movement
	char_x = (display_width * 0.45)
	char_y = (display_height * 0.8) 
	char_x_change = 0

	# Set ball position and speed
	ball_startx = random.randrange(0, display_width - 100)
	ball_starty = -600
	ball_speed = 13

	score = 0

	gameExit = False

	while not gameExit:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				# If left key, move left
				if event.key == pygame.K_LEFT and char_x - 5 >= 0:
					char_x_change = -5

				# If right, move right
				elif event.key == pygame.K_RIGHT and char_x + 5 <= 710:
					char_x_change = 5

			# Stop on release
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					char_x_change = 0			

		# Used these to avoid walls, probably a better way
		if char_x == -5:
			char_x = 0

		if char_x == 715:
			char_x = 710

		# Update x position
		if char_x >= 0 and char_x <= 710:
			char_x += char_x_change

		# Draw background
		gameDisplay.blit(background, (0,0)) 
		
		# Draw ball and move
		ball(ball_startx, ball_starty)
		ball_starty += ball_speed

		# Draw character
		char(char_x, char_y)
		score_count(score)

		# Check for collisions
		if char_y < ball_starty + 40:
			if char_x > ball_startx and char_x < ball_startx + 40 or char_x < ball_startx and char_x + 60 > ball_startx:
				hit()				

		# Reset ball at top
		if ball_starty > display_height:
			ball_starty = 0 - 100
			ball_startx = random.randrange(0, display_width - 100)
			score += 1

		pygame.display.update()

		clock.tick(60)


game_loop()
pygame.quit()
quit()