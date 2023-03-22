import pygame
import os

pygame.init()

# Set the window title and size
pygame.display.set_caption("Music Player")
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font and font size for the song title display
font = pygame.font.Font(None, 30)

# Set the directory where the music files are located
music_directory = "path/to/music/files"

# Get a list of all the music files in the directory
music_files = [os.path.join(music_directory, f) for f in os.listdir(music_directory) if f.endswith(".mp3")]

# Initialize the mixer and load the first song
pygame.mixer.init()
pygame.mixer.music.load(music_files[0])
pygame.mixer.music.play()

# Initialize some variables for tracking the current song and whether it is playing
current_song_index = 0
is_playing = True

# Create buttons for playing/pausing, skipping to the next song, and skipping to the previous song
play_pause_button = pygame.Rect(50, 400, 50, 50)
next_song_button = pygame.Rect(150, 400, 50, 50)
previous_song_button = pygame.Rect(250, 400, 50, 50)

# Start the main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Handle mouse button clicks on the buttons
            mouse_pos = event.pos

            if play_pause_button.collidepoint(mouse_pos):
                if is_playing:
                    pygame.mixer.music.pause()
                    is_playing = False
                else:
                    pygame.mixer.music.unpause()
                    is_playing = True

            if next_song_button.collidepoint(mouse_pos):
                current_song_index += 1
                if current_song_index >= len(music_files):
                    current_song_index = 0
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
                is_playing = True

            if previous_song_button.collidepoint(mouse_pos):
                current_song_index -= 1
                if current_song_index < 0:
                    current_song_index = len(music_files) - 1
                pygame.mixer.music.load(music_files[current_song_index])
                pygame.mixer.music.play()
                is_playing = True

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Get the title of the current song and display it
    current_song = os.path.basename(music_files[current_song_index])
    song_title = font.render(current_song, True, (0, 0, 0))
    screen.blit(song_title, (50, 50))

    # Draw the buttons
    pygame.draw.rect(screen, (255, 0, 0), play_pause_button)
    if is_playing:
        pygame.draw.polygon(screen, (255, 255, 255), [(play_pause_button.left + 20, play_pause_button.top + 10),
                                                       (play_pause_button.left + 20, play_pause_button.bottom - 10),
                                                       (play_pause_button.right - 10, play_pause_button.top + 25)])
    else:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(play_pause_button.left + 15, play_pause_button.top + 10, 10, 30))
        pygame.draw.rect(screen, (255, 255, 255))
