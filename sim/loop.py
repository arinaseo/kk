"""
The main simulation loop handler
"""
import pygame

import sim


def start():
    """
    Start the event loop
    :return:
    """
    while sim.running:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sim.running = False
                return
            if event.type == pygame.KEYDOWN:
                # parse key presses
                if event.key == pygame.K_ESCAPE:
                    sim.running = False
