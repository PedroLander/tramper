"""Auxiliary functions"""

def pos_to_pix(bbox, pos, size):
    """Transforms the coordinates to pixel position"""
#transform possition to pixels
    return (pos[0]-(bbox[0])-size[0]//2,
            -pos[1]+bbox[2]-size[1]//2)

def load_tile(side, bbox, screen_height, screen_width):
    """Updates the object bounding box after pressing a key"""
    match side:
        case "down":
            bbox[2]=bbox[3]
            bbox[3]=bbox[3]-screen_height
        case "up":
            bbox[3]=bbox[2]
            bbox[2]=bbox[2]+screen_height
        case "left":
            bbox[1]=bbox[0]
            bbox[0]=bbox[0]-screen_width
        case "right":
            bbox[0]=bbox[1]
            bbox[1]=bbox[1]+screen_width
