import pygame.image


class Boss:
    def __init__(self, level):
        self.hp = 50 * level
        self.level = level
        self.img = pygame.image.load(r'img/Boss.png')
        self.pos = (100, 200)

    def draw(self, screen):
        screen.blit(self.img, self.pos)


    def bite(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.level += 1
            self.hp = 50 * self.level
            return 13 * self.level
        return 0