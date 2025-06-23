import pygame, sys
from button import Button

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Buttons Tutorial")

background = pygame.image.load("Graphics/background.png").convert()

start_button = Button("Graphics/start_button.png", (300, 150), 0.65)
exit_button = Button("Graphics/exit_button.png", (300, 300), 0.65)

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	if start_button.is_pressed():
		print("Start Button pressed")

	if exit_button.is_pressed():
		pygame.quit()
		sys.exit()

	window.fill("black")
	window.blit(background, (0, 0))
	start_button.draw(window)
	exit_button.draw(window)

	pygame.display.flip()
	clock.tick(60)