import pygame
from settings import Settings

class Ship:
    """管理飞船的类"""    
    def __init__(self, settings:Settings, screen: pygame.Surface):
        """初始化飞船并设置其初始位置"""
        self.settings = settings
        self.screen = screen
        
        # 加载飞船图像并设置其大小
        self.image = pygame.image.load('images/ship.jpeg')
        # 设置图片大小为60x60像素
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # 对于每艘新飞船，都将其放在屏幕底部的中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.y = float(self.rect.bottom)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor            
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed_factor
        
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.bottom = self.y
        
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """将飞船放在屏幕底端中央"""
        self.center = self.screen_rect.centerx
        self.y = self.screen_rect.bottom    