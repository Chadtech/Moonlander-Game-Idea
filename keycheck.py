for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:

			if event.key==pygame.K_w:
				leftBack=True
				lander.image.blit(pygame.transform.flip(blast_yaw,False,True),[45,72])

			if event.key==pygame.K_k:
				leftSide=True
				lander.image.blit(pygame.transform.flip(blast_strafe,False,False),[36,67])

			if event.key==pygame.K_c:
				leftFront=True
				lander.image.blit(pygame.transform.flip(blast_yaw,False,False),[45,57])

			if event.key==pygame.K_u:
				riteBack=True
				lander.image.blit(pygame.transform.flip(blast_yaw,True,True),[92,72])

			if event.key==pygame.K_a:
				riteSide=True
				lander.image.blit(pygame.transform.flip(blast_strafe,True,False),[94,67])

			if event.key==pygame.K_b:
				riteFront=True
				lander.image.blit(pygame.transform.flip(blast_yaw,True,False),[92,57])

			if event.key==pygame.K_SPACE:
				primaryForward=True
				lander.image.blit(blast_main,[63,87])
				
				##### Without the below code, the blast would blit over the landing gear
				if landingGear in lander.storage:
					landerSprite.blit(landingGear.image,[42,74])



			if event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
				rate=16

			if event.key==pygame.K_f:
				pass

		if event.type == pygame.KEYUP:

			if event.key==pygame.K_w:
				leftBack=False

				##### landerKonstrueiren.py blits the parts of the lander onto the lander. This is different from other landeramblitting in that landerKonstrueiren.py builds the entire lander.
				execfile('landerKonstrueiren.py')
			if event.key==pygame.K_k:
				leftSide=False
				execfile('landerKonstrueiren.py')
			if event.key==pygame.K_c:
				leftFront=False
				execfile('landerKonstrueiren.py')
			if event.key==pygame.K_u:
				riteBack=False
				execfile('landerKonstrueiren.py')
			if event.key==pygame.K_a:
				riteSide=False
				execfile('landerKonstrueiren.py')
			if event.key==pygame.K_b:
				riteFront=False
				execfile('landerKonstrueiren.py')
			if event.key==pygame.K_SPACE:
				primaryForward=False
				execfile('landerKonstrueiren.py')

			if event.key==pygame.K_LSHIFT or event.key==pygame.K_RSHIFT:
				rate=1

		if event.type == pygame.QUIT:
			rungame=False
			whereAreWe=='QUITTING'