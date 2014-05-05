if lander.yPos<=400:
	lander.yPos=1200-(400-lander.yPos)
	if theWorld.yTile!=1:
		theWorld.yTile-=1

	quadUpdate()

	worldBlit(theWorld.canvas)

if lander.yPos>1200:
	lander.yPos=400+(1200-lander.yPos)
	theWorld.yTile+=1
	quadUpdate()

	worldBlit(theWorld.canvas)

if lander.xPos<=400:
	lander.xPos=1200-(400-lander.xPos)
	theWorld.xTile-=1
	quadUpdate()

	worldBlit(theWorld.canvas)

if lander.xPos>1200:
	lander.xPos=400+(1200-lander.xPos)
	theWorld.xTile+=1 

	quadUpdate()

	worldBlit(theWorld.canvas)