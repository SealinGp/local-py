import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from button import Button
from games_stats import GameStats
from settings import Settings
from ship import Ship

def check_events(settings:Settings, screen:pygame.Surface, ship:Ship, bullets:pygame.sprite.Group, play_button:Button, stats:GameStats):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)                
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)

def check_play_button(stats:GameStats, play_button:Button, mouse_x:int, mouse_y:int):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        stats.reset_stats()
        stats.game_active = True
        # 隐藏光标
        pygame.mouse.set_visible(False)
    else:
        stats.game_active = False
        # 显示光标
        pygame.mouse.set_visible(True)
           

def get_number_aliens_x(settings:Settings, alien_width:int):
    """计算每行可容纳多少个外星人"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))    
    return number_aliens_x

def create_alien(settings:Settings, screen: pygame.Surface, aliens: pygame.sprite.Group, alien_number:int, row_number:int):
    """创建一个外星人并将其加入当前行"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def get_number_rows(settings:Settings, ship_height:int, alien_height:int):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_fleet(settings:Settings, screen: pygame.Surface, ship:Ship, aliens: pygame.sprite.Group):
    """创建外星人群"""
    alien = Alien(settings, screen)
    number_aliens_x: int = get_number_aliens_x(settings, alien.rect.width)
    number_rows: int = get_number_rows(settings, ship.rect.height, alien.rect.height)
    
    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)
    

def update_screen(ai_settings:Settings, screen: pygame.Surface, ship: Ship, aliens: pygame.sprite.Group, bullets:pygame.sprite.Group,play_button:Button, stats:GameStats):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)    
    
    for bullet in bullets.sprites():        
        bullet.draw_bullet()    
        
    ship.blitme()
    aliens.draw(screen)
    
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    # 让最近绘制的屏幕可见
    pygame.display.flip()
    

def check_keydown_events(event:pygame.event.Event,settings:Settings,screen:pygame.Surface, ship:Ship, bullets:pygame.sprite.Group):
    """响应按键"""    
    move_ship(event, ship)    
    if event.key == pygame.K_SPACE:
        # 如果子弹数量小于限制，就发射一颗子弹        
        if len(bullets) < settings.bullets_allowed:
            # 创建一颗子弹，并将其加入到编组bullets中
            fire_bullet(settings, screen, ship, bullets)
        
def check_keyup_events(event:pygame.event.Event, ship:Ship):
    """响应松开"""
    move_ship(event, ship)
        

def fire_bullet(settings:Settings, screen:pygame.Surface, ship:Ship, bullets:pygame.sprite.Group):
    """如果还没有到达限制，就发射一颗子弹"""
    new_bullet = Bullet(settings, screen, ship)
    bullets.add(new_bullet)
    
    
def move_ship(event:pygame.event.Event,ship:Ship):
    """移动飞船"""
    positive_move = event.type == pygame.KEYDOWN
    if event.key == pygame.K_RIGHT:
        ship.moving_right = positive_move
    elif event.key == pygame.K_LEFT:
        ship.moving_left = positive_move
    elif event.key == pygame.K_UP:
        ship.moving_up = positive_move
    elif event.key == pygame.K_DOWN:
        ship.moving_down = positive_move    
        
        
def update_bullets(settings:Settings, screen:pygame.Surface, ship:Ship, aliens:pygame.sprite.Group, bullets:pygame.sprite.Group, stats:GameStats):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()
    clean_bullets(bullets)
    check_bullet_alien_collisions(settings, screen, ship, aliens, bullets, stats)
    
def check_bullet_alien_collisions(settings:Settings, screen:pygame.Surface, ship:Ship, aliens:pygame.sprite.Group, bullets:pygame.sprite.Group, stats:GameStats):
    """响应子弹和外星人碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)    
    if len(aliens) == 0:
        bullets.empty()
        stats.game_active = False

def clean_bullets(bullets:pygame.sprite.Group):
    """删除已消失的子弹"""
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)      
            
def update_aliens(settings:Settings, screen:pygame.Surface, ship:Ship, aliens:pygame.sprite.Group, bullets:pygame.sprite.Group, stats:GameStats):
    """更新外星人群中所有外星人的位置"""
    check_fleet_edges(settings, aliens)
    aliens.update()
    check_aliens_bottom(settings, screen, ship, aliens, bullets, stats)

    
def ship_hit(settings:Settings, screen:pygame.Surface, ship:Ship, aliens:pygame.sprite.Group, bullets:pygame.sprite.Group, stats:GameStats):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1        
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
def check_aliens_bottom(settings:Settings, screen:pygame.Surface, ship:Ship, aliens:pygame.sprite.Group, bullets:pygame.sprite.Group, stats:GameStats):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(settings, screen, ship, aliens, bullets, stats)
            break
    
    
def check_fleet_edges(settings:Settings, aliens:pygame.sprite.Group):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break
            
def change_fleet_direction(settings:Settings, aliens:pygame.sprite.Group):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1