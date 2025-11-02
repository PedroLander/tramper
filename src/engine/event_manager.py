from __future__ import annotations
import pygame
from  src.engine.funcs import move_bbox, tiles_to_pix
from typing import TYPE_CHECKING

from config import dynamic_config
if TYPE_CHECKING:
    from .level import Level
    from .layout import Layout
    from ..items.entities import Item

class EventManager():
    def __init__(self, curr_scene: Level):
        self.curr_scene = curr_scene
        self.dirs = {"down":(0,1,0),"up":(0,-1,0),"left":(-1,0,0),"right":(1,0,0)}

    def move_down(self, curr_scene):
        pass
    def jump(self, curr_scene):
        pass

    def grab(self, item1: Item, item2: Item, layout: Layout):
        self.curr_scene.tiles[item2.tile_pos].content = None
        item1.inventory.append(item2)
        item2.display=False
        item2.tile_pos = item1.tile_pos
        layout.show_msg([item2.name+" grabbed.", "Added to inventory."])

    def open_inventory(self, layout: Layout):
        layout.show_inventory(self.curr_scene.player.inventory)

    def player_move(self, direction, layout: Layout):
        if self.curr_scene.player.facing != direction:
            self.curr_scene.player.set_facing(direction)
            layout.show_msg([f"Player now faces: {direction}"])
            return

        speed = self.curr_scene.player.speed
        delta = (speed*self.dirs[direction][0],
                speed*self.dirs[direction][1],
                speed*self.dirs[direction][2])

        # Check for obstacles
        dest = tuple(
            [(a+b) for a, b in zip(self.curr_scene.player.tile_pos, delta)])
        if self.curr_scene.tiles[dest].content is not None:
                layout.show_msg(["Destination tile is not empty."])
                return
        
        # Empty origin tile content
        self.curr_scene.tiles[self.curr_scene.player.tile_pos].content = None
        # Update player's possition attribute
        self.curr_scene.player.move(delta)
        #Change plot being rendered if necesary
        if self.curr_scene.player.tile_pos not in self.curr_scene.tiles_shown:
            self.curr_scene.render_bbox = move_bbox(direction,self.curr_scene.render_bbox) # Need to add move upwards or downwards
            player_altitude = self.curr_scene.player.tile_pos[2]
            self.curr_scene.tiles_shown = tiles_to_pix(self.curr_scene.render_bbox, -player_altitude, player_altitude)
        # Fill destination tile content
        self.curr_scene.tiles[self.curr_scene.player.tile_pos].content = self.curr_scene.player
        layout.show_msg([f"Player on tile: {self.curr_scene.player.tile_pos}", 
                         f"Player on pixel: {self.curr_scene.tiles_shown[self.curr_scene.player.tile_pos].pix}"])

    def manage_event(self, keys, layout: Layout):

        if keys[pygame.K_s]:
            self.player_move("down", layout)
        if keys[pygame.K_w]:
            self.player_move("up", layout)
        if keys[pygame.K_a]:
            self.player_move("left", layout)
        if keys[pygame.K_d]:
            self.player_move("right", layout)

        if keys[pygame.K_e]:
            delta = self.dirs[self.curr_scene.player.facing]
            tile_dest: tuple = tuple(sum(t) for t in zip(self.curr_scene.player.tile_pos,delta))
            item = self.curr_scene.tiles[tile_dest].content
            if item:
                self.grab(self.curr_scene.player, item, layout)
            else:
                pass

        if keys[pygame.K_r]:
            self.open_inventory(layout)


