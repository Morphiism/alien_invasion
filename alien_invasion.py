import sys

import pygame
from settings import *
from ship import *


class AlienInvation:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invation")

        self.ship = Ship(self)

        # 设置背景色
        self.bg_color = self.settings.bg_color

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可⻅
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # 创建游戏实例并运行游戏
    ai = AlienInvation()
    ai.run_game()
