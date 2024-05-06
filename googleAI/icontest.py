import os
import pygame
import numpy as np

# Specify the file path to the MP3 file in the "music" subfolder
music_folder = "music"
mp3_file_name = "Samba Kickoff.mp3"
mp3_file_path = os.path.join(music_folder, mp3_file_name)

# Initialize Pygame
pygame.init()

# Load the MP3 file
pygame.mixer.music.load(mp3_file_path)

# Load the icon image
icon_image = pygame.image.load("good-icon.webp")

# Set up the display
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Audio Visualizer")

# Start playing the audio
pygame.mixer.music.play()

# Set up the audio analysis parameters
fps = 60
sample_rate = 44100
n_channels = 2
buffer_size = 4096

# Analyze the audio data while playing
clock = pygame.time.Clock()
while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the audio data
    audio_data = pygame.sndarray.array(pygame.sndarray.samples(buffer_size))
    audio_data = audio_data.astype(np.float32) / 32768.0  # Normalize the audio data

    # Calculate the average amplitude
    amplitude = np.mean(np.abs(audio_data))

    # Scale the icon size based on the amplitude
    icon_size = int(100 + amplitude * 200)

    # Resize the icon
    resized_icon = pygame.transform.scale(icon_image, (icon_size, icon_size))
    resized_icon_rect = resized_icon.get_rect(center=(200, 200))

    # Draw the resized icon
    screen.blit(resized_icon, resized_icon_rect)

    # Update the display
    pygame.display.flip()
    clock.tick(fps)

# Clean up
pygame.quit()