#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(1000, 800))

    def run(self, ):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass


            #for event in pygame.event.get():
             #   if event.type == pygame.QUIT:
              #      pygame.quit()  # Close Screen
               #     quit()  # End