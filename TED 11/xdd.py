import pygame
import random
import math
import time

# Inicializa o Pygame
pygame.init()

# Configurações iniciais
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Configurações de fonte
font = pygame.font.Font(None, 36)

# Cria a tela principal
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cangaceiro Matador de Demônios")

# Classe do Jogador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        original_image = pygame.image.load("Untitled.png").convert_alpha()  # Carrega a imagem original
        # Aplica o downscale de 70%
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * 0.3), int(original_image.get_height() * 0.3)))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.speed = 5
        self.health = 100

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()  # Remove o jogador quando a saúde chegar a zero

# Classe do Inimigo com IA de perseguição
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player, speed, health):
        super().__init__()
        original_image = pygame.image.load("pinho.png").convert_alpha()  # Carrega a imagem original do inimigo
        # Aplica o downscale de 70%
        self.image = pygame.transform.scale(original_image, (int(original_image.get_width() * 0.3), int(original_image.get_height() * 0.3)))
        self.rect = self.image.get_rect(center=(x, y))
        self.player = player
        self.speed = speed
        self.health = health
        self.damage = 10

    def update(self):
        dx, dy = self.player.rect.x - self.rect.x, self.player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist > 0:
            dx, dy = dx / dist, dy / dist
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

# Classe para Projéteis
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        original_image = pygame.image.load("canela.png").convert_alpha()  # Carrega a imagem do projétil
        # Aplica o downscale de 10%
        scaled_image = pygame.transform.scale(original_image, (int(original_image.get_width() * 0.1), int(original_image.get_height() * 0.1)))
        # Rotaciona a imagem 90 graus
        self.image = pygame.transform.rotate(scaled_image, 90)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10
        self.direction = direction

    def update(self):
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += self.speed * math.sin(self.direction)
        if not screen.get_rect().contains(self.rect):  # Remove projétil fora da tela
            self.kill()

# Classe Principal do Jogo
class Game:
    def __init__(self):
        self.player = Player()
        self.all_sprites = pygame.sprite.Group(self.player)
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0  # Inicia o score
        self.start_time = time.time()

        # Parâmetros de dificuldade iniciais
        self.enemy_speed = 1.5
        self.enemy_health = 30
        self.respawn_rate = 2000  # Tempo de respawn dos inimigos em milissegundos
        self.last_spawn_time = pygame.time.get_ticks()

    def spawn_enemy(self):
        x, y = random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)
        enemy = Enemy(x, y, self.player, self.enemy_speed, self.enemy_health)
        self.enemies.add(enemy)
        self.all_sprites.add(enemy)

    def increase_difficulty(self):
        # Aumenta a dificuldade a cada 30 segundos
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 30:
            self.enemy_speed += 0.5
            self.enemy_health += 10
            self.respawn_rate = max(500, self.respawn_rate - 300)  # Limite de respawn mínimo em 500ms
            self.start_time = time.time()  # Reinicia o cronômetro de dificuldade

    def run(self):
        for _ in range(5):  # Spawna inimigos iniciais
            self.spawn_enemy()
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

            # Encerra o jogo se o jogador foi eliminado
            if not self.player.alive():
                self.running = False  # Termina o loop se o jogador morrer

            # Aumenta a dificuldade com o tempo
            self.increase_difficulty()

    def events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # Verifica se a barra de espaço está pressionada para atirar
            direction = 0  # Direção fixa (direita)
            bullet = Bullet(self.player.rect.centerx, self.player.rect.centery, direction)
            self.bullets.add(bullet)
            self.all_sprites.add(bullet)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()
        self.player.update(keys)
        self.bullets.update()
        self.enemies.update()

        # Colisão entre projéteis e inimigos
        for bullet in self.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, self.enemies, False)
            for enemy in hit_enemies:
                enemy.take_damage(25)
                bullet.kill()
                if enemy.health <= 0:
                    self.score += 10  # Aumenta o score ao matar um inimigo

        # Colisão entre jogador e inimigos
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.take_damage(10)

        # Gerenciamento do respawn dos inimigos com base na dificuldade
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.respawn_rate:
            self.spawn_enemy()
            self.last_spawn_time = current_time

    def draw(self):
        screen.fill(BLACK)
        self.all_sprites.draw(screen)

        # Exibir barra de vida do jogador
        pygame.draw.rect(screen, RED, (10, 10, 100, 20))
        pygame.draw.rect(screen, GREEN, (10, 10, max(0, self.player.health), 20))

        # Exibir score
        score_text = font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

        pygame.display.flip()

# Função principal para executar o jogo
def main():
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Ocorreu um erro:", e)
