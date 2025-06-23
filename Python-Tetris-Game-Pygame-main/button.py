import pygame

class Button:
    def __init__(self, image_path, position, scale = 1.0):
        self.image = pygame.image.load(image_path).convert_alpha()
        original_width = self.image.get_width()
        original_height = self.image.get_height()
        new_width = int(original_width * scale)
        new_height = int(original_height * scale)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))
        self.rect = self.image.get_rect(topleft = position)
        self.pressed = False

    def draw(self, window):
        window.blit(self.image, self.rect)

    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if self.rect.collidepoint(mouse_pos): 
            if mouse_pressed and not self.pressed:
                self.pressed = True
                return True

        if not mouse_pressed:
            self.pressed = False 

        return False 