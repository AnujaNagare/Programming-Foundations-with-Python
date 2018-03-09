# @anuja.nagare@uga.edu
import pygame as pg

pg.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

gameDisplay = pg.display.set_mode((display_width,display_height))
pg.display.set_caption('A bit Racey')
clock = pg.time.Clock()

# pg.image.get_extended()
# carImg = pg.image.load('vehicle-clipart-front-view-7.png')

def car(x,y):
	gameDisplay.blit(carImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.85)

crashed = False

while not crashed:

	for event in pg.event.get():
		if event.type == pg.QUIT:
			crashed = True

		print(event)

	gameDisplay.fill(white)
	# car(x,y)
	pg.display.update()
	clock.tick(60)

pg.quit()
quit()

