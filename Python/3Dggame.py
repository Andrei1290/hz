import pygame 
import sys

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PLAYER_SIZE = 50
PLAYER_SPEED = 5

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Cube Game")

# Класс игрока (кубика)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ограничиваем движение игрока в пределах экрана
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Создание игрока
player = Player()

# Главный игровой цикл
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x_speed = -PLAYER_SPEED
            elif event.key == pygame.K_RIGHT:
                player.x_speed = PLAYER_SPEED
            elif event.key == pygame.K_UP:
                player.y_speed = -PLAYER_SPEED
            elif event.key == pygame.K_DOWN:
                player.y_speed = PLAYER_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.y_speed = 0

    player.update()
    screen.blit(player.image, player.rect)
    pygame.display.flip()

pygame.quit()
sys.exit()
