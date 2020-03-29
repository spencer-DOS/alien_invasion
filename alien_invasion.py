# Use tools in sys module to exit the game when someone quits.
import sys

# Pygame module contains functionality needed to make a game.
import pygame

# Create another py file (settings.py), put settings for game there and make instance here
from settings import Settings

# Create a ship.py file and import the instances for the Ship
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # Create a display window to draw all the game's graphical elements.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # Allow Ship access to game resources.
        self.ship = Ship(self)

        # Set the background color.
        self.bg_color = (50, 168, 135)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            # Draw ship on top of screen background.
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

