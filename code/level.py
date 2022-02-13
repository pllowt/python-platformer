import pygame
from support import import_csv_layout


class Level:
    def __init__(self, level_data: dict, surface):
        self.display_surface = surface

        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')

    def create_tile_group(self, layout, type):
        return 0

    def run(self):
        pass
