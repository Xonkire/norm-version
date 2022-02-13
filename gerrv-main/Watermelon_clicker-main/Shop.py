import pygame.image


class Shop:
    def __init__(self):
        self.return_button = pygame.image.load(r'img/krestik.png.')
        self.return_button_pos = (0, 0)
        self.slave_on_the_work = pygame.image.load(r'img/rab.jpg')
        self.slave_on_the_work_pos = (50, 350)
        self.bonus_k_rabu = pygame.image.load(r'img/bonus.jpg')
        self.bonus_k_rabu_pos = (50, 100)
        self.click_cost = 11
        self.DPS_cost = 1

    def try_to_buy(self, type, balance):
        if type == 'click':
            if balance >= self.click_cost:
                self.click_cost *= 2
                return balance - self.click_cost/2
        return balance


    def draw(self, screen, balance):
        screen.blit(self.return_button, self.return_button_pos)
        screen.blit(self.slave_on_the_work, self.slave_on_the_work_pos)
        screen.blit(self.bonus_k_rabu, self.bonus_k_rabu_pos)
        self.write(screen, balance)

    def write(self, screen, balance):
        font = pygame.font.Font(None, 50)
        text = font.render(f"У вас на счету: {balance} семечек", True, [255, 255, 255])
        font_pos = (100,0)
        screen.blit(text, font_pos)