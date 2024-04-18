from settings import *  # Importing settings for variables like TILE_SIZE
from os import walk
from os.path import join

def import_image(*path, alpha=True, format='png'):
    """
    Load a single image from the specified path.
    """
    full_path = join(*path) + f'.{format}'
    return pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert()

def import_folder(*path):
    """
    Load all images from a folder specified by the path.
    """
    frames = []
    for folder_path, _, image_names in walk(join(*path)):
        for image_name in sorted(image_names):
            full_path = join(folder_path, image_name)
            try:
                # Attempt to load the image
                surface = pygame.image.load(full_path).convert_alpha()
                frames.append(surface)
            except pygame.error as e:
                print(f"Error loading image {image_name}: {e}")
    return frames



def import_folder_dict(*path):
    """
    Load images from a folder into a dictionary.
    """
    frame_dict = {}
    for folder_path, _, image_names in walk(join(*path)):
        for image_name in image_names:
            full_path = join(folder_path, image_name)
            surface = pygame.image.load(full_path).convert_alpha()
            frame_dict[image_name.split('.')[0]] = surface
    return frame_dict

def import_sub_folders(*path):
    """
    Load images from subfolders into a dictionary.
    """
    frame_dict = {}
    for _, sub_folders, __ in walk(join(*path)): 
        if sub_folders:
            for sub_folder in sub_folders:
                frame_dict[sub_folder] = import_folder(*path, sub_folder)
    return frame_dict
