import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, settings:Settings, screen:pygame.Surface):
        """初始化外星人并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # 加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/alien.jpeg')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        
        # 每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height        
        self.x = float(self.rect.x)
        
    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True