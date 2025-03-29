import pygame
from button import Button
from games_stats import GameStats
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    settings = Settings()
    screen: pygame.Surface = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(settings, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    gf.create_fleet(settings, screen, ship, aliens)
    stats = GameStats(settings)
    play_button = Button(settings, screen, "Play")
    
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(settings, screen, ship, bullets, play_button, stats)
        
        if stats.game_active:
            # 更新飞船的位置
            ship.update()
            
            # 更新子弹的位置
            gf.update_bullets(settings, screen, ship, aliens, bullets, stats)
            
            # 更新外星人的位置
            gf.update_aliens(settings, screen, ship, aliens, bullets, stats)
        
        # 更新屏幕
        gf.update_screen(settings, screen, ship, aliens, bullets,play_button, stats)

      

run_game()