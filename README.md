# Particle System - Fire Simulation

This project is a simple particle system that simulates fire using Pygame. It allows you to control the size and number of particles using sliders and spawn fire particles by clicking on the screen.

## How It Was Made

1. **Pygame Initialization**: The project starts by initializing Pygame and setting up the screen dimensions and colors.
2. **Particle Class**: A `Particle` class is created to represent individual fire particles. Each particle has properties like position, size, color, speed, and lifetime.
3. **Main Loop**: The main loop handles the creation, updating, and drawing of particles. It also processes user input to spawn fire particles at the mouse position and adds GUI elements for controlling particle properties.
4. **Pygame GUI**: The `pygame_gui` library is used to add sliders for controlling the size and number of particles. Text descriptions are added to explain the sliders.
