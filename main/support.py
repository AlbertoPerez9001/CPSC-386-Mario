from os import walk
import pygame as pg

def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for img in img_files:
            full_path = path + '/' + img
            image_surf = pg.transform.rotozoom(pg.image.load(full_path),0,3)
            surface_list.append(image_surf)
    
    return surface_list