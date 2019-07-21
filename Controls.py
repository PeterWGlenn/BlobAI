
import pygame

# Controls
def controls(keys):

		if keys[pygame.K_ESCAPE]:
			return "pause"

		if keys[pygame.K_TAB]:
			return "stats"

		if keys[pygame.K_s]:
			return "showBlobAI"
