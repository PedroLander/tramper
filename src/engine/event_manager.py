import pygame
from  src.engine.funcs import move_bbox, create_tiles, tiles_to_pix

class EventManager():
    def __init__(curr_scene):
        pass
    def move_down(curr_scene):
        pass
    def jump(curr_scene):
        pass
    def check_obstacles(curr_scene):
        pass
    def manage_event(self, config, keys, curr_scene):
        ### I have to abstract this moving the repeating code to other files.
        if keys[pygame.K_DOWN]:
            curr_scene.player.set_facing("front")
            delta = (0, 1)
            # Check for obstacles
            dest = tuple(
                [(a+b) for a, b in zip(curr_scene.player.tile_pos, delta)])
            if curr_scene.tiles[dest]["content"]==None:
                # Empty origin tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=None
                # Update player's possition attribute
                curr_scene.player.move(delta)
                #Change plot being rendered if necesary
                if curr_scene.player.tile_pos[1]>curr_scene.tile_bbox_shown[3]:
                    curr_scene.tile_bbox_shown = move_bbox("down",curr_scene.tile_bbox_shown,config)
                    curr_scene.tiles_shown=create_tiles(curr_scene.tile_bbox_shown, config)
                    curr_scene.tiles_shown = tiles_to_pix(curr_scene.tile_bbox_shown, config)
                # Fill destination tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=curr_scene.player

        if keys[pygame.K_UP]:
            curr_scene.player.set_facing("back")
            delta = (0, -1)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(curr_scene.player.tile_pos, delta)])
            if curr_scene.tiles[dest]["content"]==None:
                # Empty origin tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=None
                # Update player's possition attribute
                curr_scene.player.move(delta)
                #Change plot being rendered if necesary
                if curr_scene.player.tile_pos[1]<curr_scene.tile_bbox_shown[2]:
                    curr_scene.tile_bbox_shown = move_bbox("up",curr_scene.tile_bbox_shown,config)
                    curr_scene.tiles_shown=create_tiles(curr_scene.tile_bbox_shown, config)
                    curr_scene.tiles_shown = tiles_to_pix(curr_scene.tile_bbox_shown, config)
                # Fill destination tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=curr_scene.player

        if keys[pygame.K_LEFT]:
            curr_scene.player.set_facing("left")
            delta = (-1, 0)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(curr_scene.player.tile_pos, delta)])
            if curr_scene.tiles[dest]["content"]==None:
                # Empty origin tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=None
                # Update player's possition attribute
                curr_scene.player.move(delta)
                #Change plot being rendered if necesary
                if curr_scene.player.tile_pos[0]<curr_scene.tile_bbox_shown[0]:
                    curr_scene.tile_bbox_shown = move_bbox("left",curr_scene.tile_bbox_shown,config)
                    curr_scene.tiles_shown=create_tiles(curr_scene.tile_bbox_shown, config)
                    curr_scene.tiles_shown = tiles_to_pix(curr_scene.tile_bbox_shown, config)
                # Fill destination tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=curr_scene.player

        if keys[pygame.K_RIGHT]:
            curr_scene.player.set_facing("right")
            delta = (1, 0)
            # Check for obstacles
            dest = tuple([(a+b) for a, b in zip(curr_scene.player.tile_pos, delta)])
            if curr_scene.tiles[dest]["content"]==None:
                # Empty origin tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=None
                # Update player's possition attribute
                curr_scene.player.move(delta)
                #Change plot being rendered if necesary
                if curr_scene.player.tile_pos[0]>curr_scene.tile_bbox_shown[1]:
                    curr_scene.tile_bbox_shown = move_bbox("right",curr_scene.tile_bbox_shown,config)
                    curr_scene.tiles_shown=create_tiles(curr_scene.tile_bbox_shown, config)
                    curr_scene.tiles_shown = tiles_to_pix(curr_scene.tile_bbox_shown, config)
                # Fill destination tile content
                curr_scene.tiles[curr_scene.player.tile_pos]["content"]=curr_scene.player
