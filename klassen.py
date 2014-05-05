class vessel:

	def __init__(self,xPos,yPos,xCor,yCor,xVel,yVel,angle,rotation,temp,mass,power,fuel,air,image):
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

	def obtainCargo(self,cargoItem):
		self.storage.append(cargoItem)
		self.mass+=cargoItem.mass

	def jettisonCargo(self,cargoItemNum):
		self.mass-=lander.storage[cargoItemNum].mass
		self.storage.pop(cargoItemNum)

class cargo:

	def __init__(self,mass,image,name):
		self.mass=mass
		self.image=image
		self.name=name

class place:

	def __init__(self, xSize,ySize,bgTile, minimap,sort,gravity):
		self.xSize=xSize
		self.ySize=ySize
		self.bgTile = bgTile
		self.minimap = minimap
		self.sort = sort
		self.gravity = gravity
		##### Portals is a dictionary, whoses keys are boundaries with destination values portals = { 'north':DestinationWhen(north), ..., 'planet':...}

	def ifNorth(self):
		global lander
		global northPortal
		pass

	def ifWest():
		pass

	def ifEast():
		pass

	def ifSouth():
		pass

	def ifPlanet():
		pass

class boundaries:

	def __init__(self,north,west,south,east,planet):
		self.north=north
		self.west=west
		self.south=south
		self.east=east
		self.planet=planet

class frame:

	def __init__(self,xTile,yTile,tileSprite,window,canvas):
		self.xTile=xTile
		self.yTile=yTile

		self.tileSprite=tileSprite
		self.window = window
		self.canvas = canvas
