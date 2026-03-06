import pygame
pygame.init()

class Game:

    class Player: # The player object.
        def __init__(self):
            self.y_vel = 0

    class Background: # Background object
        def __init__(self):
            self.

    class Ground: # Ground object
        def __init__(self, side):
            self.side = side

        pass

    class Solid_object_template: # Object template for solid objects.
        pass

    class Obsticale: # bad objects >:(
        pass

    class Block_transition_obj: # Fade in and out effects
        pass

    class Particle_obj: # Particle object. It can only be spawned once.
        pass

    class End_wall: # End wall for completing the level.
        pass

    class Pause_menu: # The pause menu.
        pass

    class Bot: # Background bot that competes the level with you.
        pass

    class Effects: # Other cool effects.
        pass

    # init
    def __init__(self):
        pass