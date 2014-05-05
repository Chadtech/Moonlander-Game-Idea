import os
import pygame
import math

pygame.init()

pygame.font.Font('Command-Prompt-12x16.ttf',16)
screen = pygame.display.set_mode((1600,800))
pygame.display.set_caption("ChadTech vMoonlanderGI")
clock = pygame.time.Clock()

righthandreadoutX = 1274
lefthandreadoutX = 4
statusCount = 0
gravity = 280

weakThrustPower =0.009
mainThrustPower =0.035
weakThrustRotate=0.005

rate = 1

sky = pygame.image.load('sky.png').convert()

stars = pygame.image.load('stars.png').convert()

ground = pygame.image.load('groundtile0.png').convert()

hud = pygame.image.load('hud.png').convert()
hud.set_colorkey((0,0,0,255))

scanlines = pygame.image.load('scanlines.png').convert()
scanlines.set_colorkey((0,0,0,255))

bgTile = stars

class lander:

	def __init__(self,xPos,yPos,xCor,yCor,worX,worY,xVel,yVel,angle,rotation,temp,mass,power,fuel,air,image):
		self.xPos=xPos
		self.yPos=yPos
		self.xCor=xCor
		self.yCor=yCor
		self.xVel=xVel
		self.yVel=yVel
		self.angle=angle
		self.rotation=rotation
		self.temp=temp
		self.mass=mass
		self.power=power
		self.fuel=fuel
		self.air=air
		self.image=image
		self.storage=[]

		self.image.set_colorkey((0,0,0,255))

lander = lander(1200,1200,122000,128000,0,0,0,0,0,0,128,1116.0,325.0,442941,48000,pygame.image.load('lander.png').convert())

class cargo:

	def __init__(self,weight,image,name):
		self.weight=weight
		self.image=image
		self.name=name

#Ship weight is 1116 when empty 

landingGear = cargo(837,pygame.image.load('landinggear.png').convert(),'landing gear')
landingGear.image.set_colorkey((0,0,0,255))

ballast = cargo(3627,pygame.image.load('ballast.png').convert(),'ballast')

lander.storage.append(landingGear)
lander.storage.append(ballast)

class place:

	def __init__(self, bgTile, minimap,sort,gravity):
		self.bgTile = bgTile
		self.minimap = minimap
		self.sort = sort
		self.gravity = gravity

sector0x0 = place(stars,pygame.image.load('spacemap.png').convert(),'space',280)
planet = place(sky,pygame.image.load('planetmap.png').convert(),'planet',280)

whereAreWe = sector0x0

class world:

	def __init__(self,xTile,yTile,background,frame):
		self.xTile=xTile
		self.yTile=yTile

		self.background = background
		self.frame = frame


theWorld = world(2,2,
	pygame.image.load('allthatisthecase.png').convert(),
	pygame.image.load('quadrants.png').convert(),
	)

def calculateWeight(whatsWeight):
	weight = 0
	for yit in whatsWeight.storage:
		weight += yit.weight
	return weight

def worldBlit(quadTwo,quadOne,quadThe,quadFou,window):
	window.blit(quadTwo,[0,0])
	window.blit(quadOne,[800,0])
	window.blit(quadThe,[0,800])
	window.blit(quadFou,[800,800])

def quadUpdate():
	global quadFou
	global quadThe
	global quadTwo
	global quadOne

	global theWorld

	theWorld.xTile = int(lander.xCor)/800 +1
	theWorld.yTile = int(lander.yCor)/800 +1

#	quadFou= pygame.image.load(str(theWorld.yTile)+'x'+str((theWorld.xTile))+'.png').convert()
#	quadThe= pygame.image.load(str((theWorld.yTile-1))+'x'+str((theWorld.xTile))+'.png').convert()
#	quadTwo= pygame.image.load(str((theWorld.yTile-1))+'x'+str((theWorld.xTile-1))+'.png').convert()
#	quadOne= pygame.image.load(str(theWorld.yTile)+'x'+str((theWorld.xTile-1))+'.png').convert()

	quadFou= whereAreWe.bgTile
	quadThe= whereAreWe.bgTile
	quadTwo= whereAreWe.bgTile
	quadOne= whereAreWe.bgTile


quadUpdate()

blast_strafe = pygame.image.load('blast_strafe.png').convert()
blast_yaw = pygame.image.load('blast_yaw.png').convert()
blast_main = pygame.image.load('blast_main.png').convert()

landinggear = pygame.image.load('landinggear.png').convert()

landinggear.set_colorkey((0,0,0,255))
blast_main.set_colorkey((0,0,0,255))

worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

rungame = True

LF=False
LS=False
LB=False

RF=False
RS=False
RB=False

mainThrust = False

while rungame:
	for event in pygame.event.get():
		#pressed = pygame.key.get_pressed()

		if event.type == pygame.KEYDOWN:

			if event.key==pygame.K_w:
				LB=True
			if event.key==pygame.K_a:
				LS=True
			if event.key==pygame.K_c:
				LF=True
			if event.key==pygame.K_u:
				RB=True
			if event.key==pygame.K_k:
				RS=True
			if event.key==pygame.K_b:
				RF=True
			if event.key==pygame.K_SPACE:
				mainThrust=True

			if event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
				rate=16

			if event.key==pygame.K_f:
				distfromCenter

			if event.key==pygame.K_ESCAPE:
				rungame=False

		if event.type == pygame.KEYUP:

			if event.key==pygame.K_w:
				LB=False
			if event.key==pygame.K_a:
				LS=False
			if event.key==pygame.K_c:
				LF=False
			if event.key==pygame.K_u:
				RB=False
			if event.key==pygame.K_k:
				RS=False
			if event.key==pygame.K_b:
				RF=False
			if event.key==pygame.K_SPACE:
				mainThrust=False

			if event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
				rate=1

		if event.type == pygame.QUIT:
			rungame=False

		lander.image = pygame.image.load('lander.png').convert()

	if lander.fuel>0:
		if mainThrust:
			lander.xVel-=(mainThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.yVel-=(mainThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.image.blit(blast_main,[63,87])
			lander.fuel-=19*rate

		if LB:
			lander.xVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.yVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.rotation-=weakThrustRotate*rate
			lander.image.blit(pygame.transform.flip(blast_yaw,False,True),[45,72])
			lander.fuel-=9*rate

		if LS:
			lander.yVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.xVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.image.blit(pygame.transform.flip(blast_strafe,True,False),[94,67])
			lander.fuel-=9*rate

		if LF:
			lander.yVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.xVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.rotation+=weakThrustRotate*rate
			lander.image.blit(pygame.transform.flip(blast_yaw,False,False),[45,57])
			lander.fuel-=9*rate

		if RB:
			lander.yVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.xVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.rotation+=weakThrustRotate*rate
			lander.image.blit(pygame.transform.flip(blast_yaw,True,True),[92,72])
			lander.fuel-=9*rate

		if RS:
			lander.yVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.xVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.image.blit(pygame.transform.flip(blast_strafe,False,False),[36,67])
			lander.fuel-=9*rate

		if RF:
			lander.yVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate
			lander.xVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate
			lander.rotation-=weakThrustRotate*rate
			lander.image.blit(pygame.transform.flip(blast_yaw,True,False),[92,57])
			lander.fuel-=9*rate

	else:
			lander.fuel=0

	if landingGear in lander.storage:
		lander.image.blit(landingGear.image,[42,74])

	if lander.yPos<=400:
		lander.yPos=1200-(400-lander.yPos)
		if theWorld.yTile!=1:
			theWorld.yTile-=1

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	if lander.yPos>1200:
		lander.yPos=400+(1200-lander.yPos)
		theWorld.yTile+=1

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	if lander.xPos<=400:
		lander.xPos=1200-(400-lander.xPos)
		theWorld.xTile-=1

		quadUpdate()

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	if lander.xPos>1200:
		lander.xPos=400+(1200-lander.xPos)
		theWorld.xTile+=1 

		worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	distfromCenter=(((128000-(lander.yCor))**2)+((128000-lander.xCor)**2))**(0.5)

	if distfromCenter>3000:
		gravDir=0
		if lander.xCor<128000 and lander.yCor<128000:
			gravDir = math.degrees(math.atan((lander.xCor-128000)/(lander.yCor-128000)))%90
		if lander.xCor>128000 and lander.yCor<128000:
			gravDir = math.degrees(math.atan((lander.xCor-128000)/(lander.yCor-128000)))%90 + 270
		if lander.xCor>128000 and lander.yCor>128000:
			gravDir = math.degrees(math.atan((lander.xCor-128000)/(lander.yCor-128000)))%90 + 180
		if lander.xCor<128000 and lander.yCor>128000:
			gravDir = math.degrees(math.atan((lander.xCor-128000)/(lander.yCor-128000)))%90 + 90

		lander.yVel+=(gravity/distfromCenter)*math.cos(math.radians(gravDir))
		lander.xVel+=(gravity/distfromCenter)*math.sin(math.radians(gravDir))
	else:
		lander.yVel+=gravity/distfromCenter

	if distfromCenter<3000:
		whereAreWe = planet
	else:
		whereAreWe = sector0x0
		
	lander.angle+=lander.rotation

	lander.xPos+=lander.xVel
	lander.yPos+=lander.yVel

	lander.xCor+=lander.xVel
	lander.yCor+=lander.yVel

	if statusCount<50:
		statusCount+=1
	else:
		statusCount=0
		lander.air-=1

		#quadUpdate()

		#worldBlit(quadTwo,quadOne,quadThe,quadFou,theWorld.frame)

	worldX, worldY = pygame.transform.rotate(theWorld.background,lander.angle).get_size()
	worldX = worldX/2 
	worldY = worldY/2

	lander.image.set_colorkey((0,0,0,255))

	# below. However the line of code below might still be important later
	# frame.blit(pygame.transform.rotate(lander,angle),[cordX-landX,cordY-landY])

	theWorld.background.blit(theWorld.frame,[-lander.xPos+400,-lander.yPos+400])

	screen.blit(pygame.transform.rotate(theWorld.background,-lander.angle),[(800-worldX),400-worldY])
	screen.blit(lander.image,[731,331])
	screen.blit(hud,[0,0])

	# Minimap
	screen.blit(whereAreWe.minimap,[1272,2])

	if whereAreWe.sort=='space':
		screen.set_at((1275+(int(lander.xCor/800)),5+(int(lander.yCor/800))),(255,255,255))
	elif whereAreWe.sort=='planet':
		screen.blit(pygame.transform.scale(lander.image,(10,10)),[1275+(int(lander.xCor/18400)),5+(int(lander.yCor/18400))])

	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',32).render('> ChadTech MLGI',False,(255,255,255)),[4,4])

	#Read outs
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> DATA READOUT :',False,(255,255,255)),[righthandreadoutX,333])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Pos(x,y) = ('+str(int(theWorld.xTile))+', '+str(int(theWorld.yTile))+')',False,(255,255,255)),[righthandreadoutX,349])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Vel(x,y) = ('+str(int(10*lander.xVel))+', '+str(int(10*lander.yVel))+')',False,(255,255,255)),[righthandreadoutX,365])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Velocity = '+str(int(10*(((lander.yVel**2)+(lander.xVel**2))**(0.5))))+' Ppc',False,(255,255,255)),[righthandreadoutX,381])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Ang Vel  = '+str(round(lander.rotation*10,1))+' Dpc',False,(255,255,255)),[righthandreadoutX,397])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Angle    = '+str((int(lander.angle%360))).zfill(3)+' *',False,(255,255,255)),[righthandreadoutX,413])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Dir      = ##SYS ERR',False,(255,255,255)),[righthandreadoutX,429])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Ext Temp = ' +'UNAVAIL',False,(255,255,255)),[righthandreadoutX,445])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('>',False,(255,255,255)),[righthandreadoutX,461])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> TWIN KILLER STATUS :',False,(255,255,255)),[righthandreadoutX,477])
	#The name of the ship is 'Twin Killer'
	# Alternative name ideas????
	# 0. Forbes
	# 1. Frege
	# 2. Recalcritrant
	# 3. Referenten
	# 4. Bedeutung
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Int Temp = '+str(lander.temp)+' cT',False,(255,255,255)),[righthandreadoutX,493])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Mass     = '+str(round(lander.mass,2))+' Slb',False,(255,255,255)),[righthandreadoutX,509])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Power    = '+str(round(lander.power,2))+' hp/d',False,(255,255,255)),[righthandreadoutX,525])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Oxygen   = '+str(round(lander.air/10.0,1))+' gpi',False,(255,255,255)),[righthandreadoutX,541])
	screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Kerosene = '+str(round(lander.fuel/100.0,1))+' gpi',False,(255,255,255)),[righthandreadoutX,557])

	#Cargo
	#screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> INVENTORY :',False,(255,255,255)),[lefthandreadoutX,36])
	#for yit in range(42):
	#	if yit < len(lander.storage):
	#		screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> '+str(yit).zfill(2)+') '+lander.storage[yit].name,False,(255,255,255)),[lefthandreadoutX,52+(yit*16)])
	#	else: 
	#		screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> '+str(yit).zfill(2)+') '+'EMPTY',False,(255,255,255)),[lefthandreadoutX,52+(yit*16)])

		#Scan Lines
	screen.blit(scanlines,[0,0])

	pygame.display.flip()
	clock.tick(60)

pygame.quit()