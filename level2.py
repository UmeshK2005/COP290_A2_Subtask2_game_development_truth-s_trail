import pygame
import pytmx
from pytmx.util_pygame import load_pygame

# Constants
SCROLL_SPEED = 5  # Adjust as needed

def load_map(tmx_file):
    tmx_data = load_pygame(tmx_file)
    return tmx_data

def draw_tiles(screen, tmx_data, scroll_x, scroll_y):
    tile_width_half = tmx_data.tilewidth // 2
    tile_height_half = tmx_data.tileheight // 2
    map_width = tmx_data.width * tmx_data.tilewidth
    map_height = tmx_data.height * tmx_data.tileheight

    for layer in tmx_data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_data.get_tile_image_by_gid(gid)
                if tile:
                    # Convert orthogonal coordinates to isometric
                    iso_x = (x - y) * tile_width_half
                    iso_y = (x + y) * tile_height_half
                    # Center the map on screen
                    screen_x = (screen.get_width() // 2) - (map_width // 4) + iso_x - scroll_x
                    screen_y = (screen.get_height() // 2) - (map_height // 4) + iso_y - scroll_y

                    screen.blit(tile, (screen_x, screen_y))

def draw_standalone_objects(screen, tmx_data, scroll_x, scroll_y):
    for layer in tmx_data.layers:
        if isinstance(layer, pytmx.TiledObjectGroup):
            for obj in layer:
                if hasattr(obj, "image") and obj.image:
                    screen_x, screen_y = obj.x - scroll_x, obj.y - scroll_y

                    # Check if the position is within the screen bounds
                    if 0 <= screen_x <= screen.get_width() and 0 <= screen_y <= screen.get_height():
                        screen.blit(obj.image, (screen_x, screen_y))

def level2_game(screen, screen_width, screen_height):
    pygame.init()

    tmx_data = load_map('final_map1.tmx')

    running = True
    scroll_x, scroll_y = 0, 0  # Initial scroll position
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    scroll_x += SCROLL_SPEED
                elif event.key == pygame.K_RIGHT:
                    scroll_x -= SCROLL_SPEED
                elif event.key == pygame.K_UP:
                    scroll_y += SCROLL_SPEED
                elif event.key == pygame.K_DOWN:
                    scroll_y -= SCROLL_SPEED

        screen.fill((0, 0, 0))  # Clear the screen with black
        draw_tiles(screen, tmx_data, scroll_x, scroll_y)  # Draw the tile layers
        draw_standalone_objects(screen, tmx_data, scroll_x, scroll_y)  # Draw the standalone image objects

        pygame.display.flip()

    pygame.quit()


# For testing
if __name__ == "__main__":
    pygame.init()
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600  # Define your screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level 2")

    level2_game(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
