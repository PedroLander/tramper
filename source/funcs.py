def pos_to_pix(bbox, pos, size):
#transform possition to pixels
    return (pos[0]-(bbox[0])-size[0]//2,
            -pos[1]+bbox[2]-size[1]//2)

