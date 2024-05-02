import pygame

# Initialize Pygame
pygame.init()

# Load the MP3 file
pygame.mixer.music.load(temp_file_path)

# Load the icon image
icon_image = pygame.image.load("path/to/icon_image.png")

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Audio Playback with Icon Animation")

# Start playing the audio
pygame.mixer.music.play()

# Animate the icon while the audio is playing
clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Rotate the icon
    rotated_icon = pygame.transform.rotate(icon_image, pygame.time.get_ticks() / 50)
    rotated_icon_rect = rotated_icon.get_rect(center=(200, 200))

    # Draw the rotated icon
    screen.blit(rotated_icon, rotated_icon_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()