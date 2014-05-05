landerSprite = pygame.image.load('lander.png').convert()

if primaryForward:
	landerSprite.blit(blast_main,[63,87])

if leftFront:
	landerSprite.blit(pygame.transform.flip(blast_yaw,False,False),[45,57])
if leftSide:
	landerSprite.blit(pygame.transform.flip(blast_strafe,True,False),[94,67])
if leftBack:
	landerSprite.blit(pygame.transform.flip(blast_yaw,False,True),[45,72])

if riteFront:
	landerSprite.blit(pygame.transform.flip(blast_yaw,True,False),[92,57])
if riteSide:
	landerSprite.blit(pygame.transform.flip(blast_strafe,False,False),[36,67])
if riteBack:
	landerSprite.blit(pygame.transform.flip(blast_yaw,True,True),[92,72])

if landingGear in lander.storage:
	landerSprite.blit(landingGear.image,[42,74])

lander.image = landerSprite