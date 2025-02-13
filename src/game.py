import pygame
from sprites import Player, Coin, Obstacle
from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Coin Collector")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.game_over = False
        
        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        
        self.player = Player()
        self.all_sprites.add(self.player)
        
        # Create initial coins and obstacles
        for _ in range(5):
            self.spawn_coin()
        for _ in range(3):
            self.spawn_obstacle()
    
    def spawn_coin(self):
        coin = Coin()
        self.all_sprites.add(coin)
        self.coins.add(coin)
    
    def spawn_obstacle(self):
        obstacle = Obstacle()
        self.all_sprites.add(obstacle)
        self.obstacles.add(obstacle)
    
    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            if not self.game_over:
                self.update()
            self.draw()
        
        pygame.quit()
    
    def update(self):
        self.all_sprites.update()
        
        # Check coin collisions
        coin_hits = pygame.sprite.spritecollide(self.player, self.coins, True)
        for coin in coin_hits:
            self.score += 1
            self.spawn_coin()
        
        # Check obstacle collisions
        if pygame.sprite.spritecollide(self.player, self.obstacles, False):
            self.game_over = True
    
    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        if self.game_over:
            game_over_text = self.font.render("Game Over!", True, WHITE)
            self.screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        
        pygame.display.flip() 
