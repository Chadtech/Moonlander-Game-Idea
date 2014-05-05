
##### The program needs to know where the center of theWorld is, because the center does not change when the image grows
worldX, worldY = pygame.transform.rotate(theWorld.window,lander.angle).get_size()
worldX = worldX/2 
worldY = worldY/2

##### This is a candidate for removal:
lander.image.set_colorkey((0,0,0,255))

# below. However the line of code below might still be important later
# canvas.blit(pygame.transform.rotate(lander,angle),[cordX-landX,cordY-landY])

#####Paste the enormous canvas onto the smaller world
theWorld.window.blit(theWorld.canvas,[-lander.xPos+400,-lander.yPos+400])

##### Put theWorld onto the screen
screen.blit(pygame.transform.rotate(theWorld.window,-lander.angle),[(800-worldX),400-worldY])
##### Put the lander onto the screen, the important-later lines above put the lander onto theWorld. Both work, but this one makes a clearer image.
screen.blit(lander.image,[731,331])
##### Put the Hud onto the screen
screen.blit(hud,[0,0])

##### Minimap
screen.blit(whereAreWe.minimap,[1272,2])

##### Accurate lander placement given whereWeAre type
if whereAreWe.sort=='space':
	screen.set_at((1275+(int(lander.xCor/800)),5+(int(lander.yCor/800))),(255,255,255))
elif whereAreWe.sort=='planet':
	screen.blit(pygame.transform.scale(lander.image,(10,10)),[1275+(int(lander.xCor/800)*(18400/256000)),5+(int(lander.yCor/800)*(18400/256000))])


screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',32).render('> ChadTech MLGI',False,(255,255,255)),[4,4])

#Read outs
screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> DATA READOUT :',False,(255,255,255)),[righthandreadoutX,333])
screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Pos(x,y) = ('+str(int(theWorld.xTile))+', '+str(int(theWorld.yTile))+')',False,(255,255,255)),[righthandreadoutX,349])
screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Vel(x,y) = ('+str(int(10*lander.xVel))+', '+str(int(10*lander.yVel))+')',False,(255,255,255)),[righthandreadoutX,365])
screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Velocity = '+str(int(10*(((lander.yVel**2)+(lander.xVel**2))**(0.5))))+' Ppc',False,(255,255,255)),[righthandreadoutX,381])
screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Ang Vel  = '+str(round(lander.rotation*10,1)).zfill(3)+' Dpc',False,(255,255,255)),[righthandreadoutX,397])
screen.blit(pygame.font.Font('Command-Prompt-12x16.ttf',16).render('> Angle    = '+str((int(lander.angle%360))).zfill(3)+' D',False,(255,255,255)),[righthandreadoutX,413])
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