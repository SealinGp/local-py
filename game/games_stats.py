from settings import Settings


class GameStats():
    """跟踪游戏的统计信息"""
    
    def __init__(self, settings:Settings):
        """初始化统计信息"""
        self.game_active = False
        self.settings = settings
        self.reset_stats()
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
    