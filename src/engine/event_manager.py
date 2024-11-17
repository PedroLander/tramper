import pygame
from  src.engine.funcs import move_bbox, create_tiles, tiles_to_pix

class EventManager():
    def __init__(self, curr_scene):
        self.curr_scene = curr_scene
        self.dirs = {"down":(0,1,0),"up":(0,-1,0),"left":(-1,0,0),"right":(1,0,0)}

    def move_down(curr_scene):
        pass
    def jump(curr_scene):
        pass
    def check_obstacles(curr_scene):
        pass
    def grab(self, item1, item2, panel):
        self.curr_scene.tiles[item2.tile_pos]["content"]=None
        item1.inventory.append(item2)
        item2.display=False
        item2.tile_pos = item1.tile_pos
        panel.show_msg(item2.name+" grabbed. Added to inventory.")

    def arrow_stroke(self, direction, config, panel):
        self.curr_scene.player.set_facing(direction)
        speed = self.curr_scene.player.speed
        delta = (speed*self.dirs[direction][0],
                 speed*self.dirs[direction][1],
                 speed*self.dirs[direction][2])

        # Check for obstacles
        dest = tuple(
            [(a+b) for a, b in zip(self.curr_scene.player.tile_pos, delta)])
        if self.curr_scene.tiles[dest]["content"]==None:
                # Empty origin tile content
                self.curr_scene.tiles[self.curr_scene.player.tile_pos]["content"]=None
                # Update player's possition attribute
                self.curr_scene.player.move(delta)
                #Change plot being rendered if necesary
                if direction=="down" and self.curr_scene.player.tile_pos[1]<=self.curr_scene.tile_bbox_shown[3]:
                    pass
                elif direction=="up" and self.curr_scene.player.tile_pos[1]>=self.curr_scene.tile_bbox_shown[2]:
                    pass
                elif direction=="left" and self.curr_scene.player.tile_pos[0]>=self.curr_scene.tile_bbox_shown[0]:
                    pass
                elif direction=="right" and self.curr_scene.player.tile_pos[0]<=self.curr_scene.tile_bbox_shown[1]:
                    pass
                else:
                    self.curr_scene.tile_bbox_shown = move_bbox(direction,self.curr_scene.tile_bbox_shown,config)
                    self.curr_scene.tiles_shown=create_tiles(self.curr_scene.tile_bbox_shown)
                    self.curr_scene.tiles_shown = tiles_to_pix(self.curr_scene.tile_bbox_shown, config)
                # Fill destination tile content
                self.curr_scene.tiles[self.curr_scene.player.tile_pos]["content"]=self.curr_scene.player

    def manage_event(self, config, keys, panel):

        if keys[pygame.K_DOWN]:
            self.arrow_stroke("down", config, panel)
        if keys[pygame.K_UP]:
            self.arrow_stroke("up", config, panel)
        if keys[pygame.K_LEFT]:
            self.arrow_stroke("left", config, panel)
        if keys[pygame.K_RIGHT]:
            self.arrow_stroke("right", config, panel)

        if keys[pygame.K_e]:
            delta = self.dirs[self.curr_scene.player.facing]
            tile_dest = tuple(sum(t) for t in zip(self.curr_scene.player.tile_pos,delta))
            item = self.curr_scene.tiles[tile_dest]["content"]
            if item:
                self.grab(self.curr_scene.player, item, panel)
            else:
                panel.show_msg("Nothing to grab.")
