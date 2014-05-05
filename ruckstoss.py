if lander.fuel>0:
	if primaryForward:
		lander.xVel-=(primaryForwardPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.yVel-=(primaryForwardPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
		#lander.image.blit(blast_main,[63,87])
		lander.fuel-=19*rate
	if leftBack:
		lander.xVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.yVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.rotation-=weakThrustRotate*rate
		#lander.image.blit(pygame.transform.flip(blast_yaw,False,True),[45,72])
		lander.fuel-=9*rate
	if leftSide:
		lander.yVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.xVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
		#lander.image.blit(pygame.transform.flip(blast_strafe,True,False),[94,67])
		lander.fuel-=9*rate
	if leftFront:
		lander.yVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.xVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.rotation+=weakThrustRotate*rate
		#lander.image.blit(pygame.transform.flip(blast_yaw,False,False),[45,57])
		lander.fuel-=9*rate
	if riteBack:
		lander.yVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.xVel-=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.rotation+=weakThrustRotate*rate
	#	lander.image.blit(pygame.transform.flip(blast_yaw,True,True),[92,72])
		lander.fuel-=9*rate
	if riteSide:
		lander.yVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.xVel-=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
	#	lander.image.blit(pygame.transform.flip(blast_strafe,False,False),[36,67])
		lander.fuel-=9*rate
	if riteFront:
		lander.yVel+=(weakThrustPower*math.cos(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.xVel+=(weakThrustPower*math.sin(math.radians(lander.angle)))*rate*(11160/lander.mass)
		lander.rotation-=weakThrustRotate*rate
	#	lander.image.blit(pygame.transform.flip(blast_yaw,True,False),[92,57])
		lander.fuel-=9*rate

else:
	lander.fuel=0