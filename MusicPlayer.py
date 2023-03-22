import pygame

# Initialize Pygame
pygame.init()

# Load music file
pygame.mixer.music.load("music.mp3")

# Set up screen and font
screen = pygame.display.set_mode((300, 100))
font = pygame.font.SysFont("Arial", 20)

# Set up control buttons
play_button = pygame.Rect(50, 50, 50, 50)
pause_button = pygame.Rect(110, 50, 50, 50)
stop_button = pygame.Rect(170, 50, 50, 50)

# Main loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if control button is clicked
            if play_button.collidepoint(event.pos):
                pygame.mixer.music.play()
            elif pause_button.collidepoint(event.pos):
                pygame.mixer.music.pause()
            elif stop_button.collidepoint(event.pos):
                pygame.mixer.music.stop()

    # Draw control buttons
    pygame.draw.rect(screen, (0, 255, 0), play_button)
    pygame.draw.rect(screen, (255, 255, 0), pause_button)
    pygame.draw.rect(screen, (255, 0, 0), stop_button)

    # Draw button labels
    screen.blit(font.render("Play", True, (255, 255, 255)), (55, 65))
    screen.blit(font.render("Pause", True, (255, 255, 255)), (115, 65))
    screen.blit(font.render("Stop", True, (255, 255, 255)), (175, 65))

    # Update screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
