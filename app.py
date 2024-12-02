import pygame
import random
import pygame_gui

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle System - Fire Simulation")

# Colors
BLACK = (0, 0, 0)
FIRE_COLORS = [(255, 69, 0), (255, 140, 0), (255, 215, 0)]

# Particle class
class Particle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color  # Ensure color is set correctly
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-3, -1)
        self.lifetime = random.randint(20, 50)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1
        self.size = max(0, self.size - 0.1)

    def draw(self, screen):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.size))

# Main loop
def main():
    clock = pygame.time.Clock()
    particles = []
    fire_positions = []
    running = True

    # Initialize Pygame GUI
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    size_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((10, 10), (200, 30)),
        start_value=5,
        value_range=(1, 10),
        manager=manager
    )
    count_slider = pygame_gui.elements.UIHorizontalSlider(
        relative_rect=pygame.Rect((10, 50), (200, 30)),
        start_value=5,
        value_range=(1, 20),
        manager=manager
    )
    color_dropdown = pygame_gui.elements.UIDropDownMenu(
        options_list=['Red', 'Orange', 'Yellow'],
        starting_option='Red',
        relative_rect=pygame.Rect((10, 90), (200, 30)),
        manager=manager
    )
    reset_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((10, 130), (200, 30)),
        text='Reset',
        manager=manager
    )

    # Font for text
    font = pygame.font.Font(None, 24)

    while running:
        time_delta = clock.tick(60) / 1000.0
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Add fire position on mouse click
                fire_positions.append(pygame.mouse.get_pos())
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == reset_button:
                    particles.clear()
                    fire_positions.clear()
            manager.process_events(event)

        manager.update(time_delta)

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Get slider values
        particle_size = size_slider.get_current_value()
        particle_count = int(count_slider.get_current_value())

        # Get selected color
        selected_color = color_dropdown.selected_option[0]  # Extract the correct value
        if selected_color == 'Red':
            particle_color = (255, 69, 0)
        elif selected_color == 'Orange':
            particle_color = (255, 140, 0)
        else:
            particle_color = (255, 215, 0)

        # Generate new particles at mouse position and fire positions
        for pos in [(mouse_x, mouse_y)] + fire_positions:
            for _ in range(particle_count):
                particles.append(Particle(pos[0], pos[1], particle_size, particle_color))

        # Update and draw particles
        for particle in particles[:]:
            particle.update()
            particle.draw(screen)
            if particle.lifetime <= 0:
                particles.remove(particle)

        # Draw the UI manager
        manager.draw_ui(screen)

        # Draw text descriptions
        size_text = font.render("Particle Size", True, (255, 255, 255))
        count_text = font.render("Particle Count", True, (255, 255, 255))
        color_text = font.render("Particle Color", True, (255, 255, 255))
        screen.blit(size_text, (220, 10))
        screen.blit(count_text, (220, 50))
        screen.blit(color_text, (220, 90))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
