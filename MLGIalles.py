import os
import pygame
import math

pygame.init()

terminalFont = pygame.font.Font('Command-Prompt-12x16.ttf',16)
screen = pygame.display.set_mode((1600,800))
pygame.display.set_caption("ChadTech vMoonlanderGI")
clock = pygame.time.Clock()

##### These variables are useful for blitting text onto the screen
righthandreadoutX = 1274
lefthandreadoutX = 4

##### These are for counting, so the ship is updated at a reasonable pace
statusCount = 0
countUpdate = 50

##### Thruster strengths
weakThrustPower =0.009
primaryForwardPower =0.035
weakThrustRotate=0.005

##### Fuel consumption rate
rate = 1

##### Images
sky = pygame.image.load('sky.png').convert()

stars = pygame.image.load('stars.png').convert()

ground = pygame.image.load('groundtile0.png').convert()

hud = pygame.image.load('hud.png').convert()
hud.set_colorkey((0,0,0,255))

scanlines = pygame.image.load('scanlines.png').convert()
scanlines.set_colorkey((0,0,0,255))

blast_strafe = pygame.image.load('blast_strafe.png').convert()
blast_yaw = pygame.image.load('blast_yaw.png').convert()
blast_main = pygame.image.load('blast_main.png').convert()
blast_strafe.set_colorkey((0,0,0,255))
blast_yaw.set_colorkey((0,0,0,255))
blast_main.set_colorkey((0,0,0,255))

##### Import classes
execfile('klassen.py')

##### This is the lander
lander = vessel(1200,1200,122000,128000,0,0,0,0,128,1116.0,325.0,442941,48000,pygame.image.load('lander.png').convert())
#Ship weight is 1116 when empty, 11160 is my target medium weight


##### These are cargo items

landingGear = cargo(837,pygame.image.load('landinggear.png').convert(),'landing gear')
landingGear.image.set_colorkey((0,0,0,255))

ballast = cargo(3627,pygame.image.load('ballast.png').convert(),'ballast')

###### 

execfile('funktionen.py')

##### Add some starting cargo
lander.obtainCargo(landingGear)
lander.obtainCargo(ballast)

whereAreWe=0

##### Define a few places
sector0x0 = place(256000,256000,stars,pygame.image.load('spacemap.png').convert(),'space',280)
planet = place(184000,184000,sky,pygame.image.load('planetmap.png').convert(),'planet',280)


northPortals = {
	sector0x0:sector0x0
}

##### We need a variable to point to whereWeAre. Its easier to make the pointer point to what kind of place we are in, than change the 'laws of physics'
whereAreWe = sector0x0

quadFou= whereAreWe.bgTile
quadThe= whereAreWe.bgTile
quadTwo= whereAreWe.bgTile
quadOne= whereAreWe.bgTile

#####
theWorld = frame(2,2,
	whereAreWe.bgTile,
	pygame.image.load('allthatisthecase.png').convert(),
	pygame.image.load('quadrants.png').convert(),
	)

quadUpdate()

worldBlit(theWorld.canvas)

##### When rungame is false, the game ends
rungame = True

##### These booleans correspond to whether the thruster is firing or not. The variable name is the position of the thruster on the ship, not in which direction it thrusts the ship
leftFront=False
leftSide=False
leftBack=False

riteFront=False
riteSide=False
riteBack=False

primaryForward=False

execfile('landerKonstrueiren.py')
while rungame:
	
	while whereAreWe.sort=='space':	
		##### Check for key presses, and change the corresponding variables
		execfile('keycheck.py')

		#lander.image = pygame.image.load('lander.png').convert()

		###### Update state of acceleration
		execfile('ruckstoss.py')

		###### Update quadrant location
		execfile('weltBericht.py')

		###### Update the physics
		execfile('physikBericht.py')

		###### Update the lander status (like oxygen)
		execfile('landerBericht.py')

		##### Blitting the screen
		execfile('blitter.py')

pygame.quit()

