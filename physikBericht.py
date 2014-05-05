if whereAreWe.sort == 'space':

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

		lander.yVel+=(whereAreWe.gravity/distfromCenter)*math.cos(math.radians(gravDir))
		lander.xVel+=(whereAreWe.gravity/distfromCenter)*math.sin(math.radians(gravDir))

	else:
		lander.yVel+=whereAreWe.gravity/distfromCenter

	if distfromCenter<3000:
		whereAreWe=planet
		lander.yCor = 0
		print gravDir/360*18400, lander.yVel, lander.xVel
		lander.xCor = (gravDir/360)*18400

		lander.yVel=0
		lander.xVel=0

		## x,y velocities need to be adjusted based on whether the lander was entering the planet head on, or tangently
		#lander.yVel = (((lander.yVel**2)+(lander.xVel**2))**(0.5))*math.cos(math.radians(lander.angle-gravDir))

		#lander.angle = lander.angle-gravDir
		#whereAreWe = planet

	sector0x0Bou()

elif whereAreWe.sort== 'planet':
	##### 50 is a place holder until I really figure out how high the ground is from the bottom of the map
	try:
		lander.yVel+=whereAreWe.gravity/(18400-lander.yCor)
		print lander.yVel
	except:
		lander.yVel+=0.01

	lander.yVel=lander.yVel*0.99
	lander.xVel=lander.xVel*0.99

	if lander.yCor<0:
		lander.yCor=3000*math.cos(((lander.xCor-128000/18400)*360))
		lander.xCor=3000*math.sin(((lander.xCor/184000)*360))
		whereAreWe=sector0x0
	if lander.yCor>18200:
		lander.yVel=0
		lander.xVel=0
		lander.rotation=0
			
lander.angle+=lander.rotation
lander.xPos+=lander.xVel
lander.yPos+=lander.yVel
lander.xCor+=lander.xVel
lander.yCor+=lander.yVel