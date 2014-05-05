def obtainCargo(lander,cargoItem):
	lander.storage.append(cargoItem)
	lander.mass+=cargoItem.mass

def jettisonCargo(lander,cargoItemNum):
	lander.mass-=lander.storage[cargoItemNum].mass
	lander.storage.pop(cargoItemNum)

def worldBlit(window):
	global quadFou
	global quadThe
	global quadTwo
	global quadOne

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

	global whereAreWe

	#global lander

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

def sector0x0Bou():
	global lander
	global whereAreWe

	if lander.yCor<0:
		lander.yCor+=whereAreWe.ySize
	if lander.xCor<0:
		lander.xCor+=whereAreWe.xSize
	if lander.yCor>whereAreWe.ySize:
		lander.yCor-=whereAreWe.ySize
	if lander.xCor>whereAreWe.xSize:
		lander.xCor-=whereAreWe.xSize