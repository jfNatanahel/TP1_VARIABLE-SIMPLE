import pygame
import sys

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
width, height = 800, 600

# Crea la ventana de visualización
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulación de Holograma")

# Color de fondo
background_color = (0, 0, 0)

# Ciclo principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dibuja el fondo
    screen.fill(background_color)

    # Simula un objeto "holográfico"
    hologram_color = (0, 0, 255)
    hologram_radius = 50
    hologram_position = (width // 2, height // 2)
    pygame.draw.circle(screen, hologram_color, hologram_position, hologram_radius)

    # Actualiza la ventana
    pygame.display.flip()

# Cierra Pygame
pygame.quit()
sys.exit()