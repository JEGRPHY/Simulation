import numpy as np
import pygame

class ParticleSimulation:
    def __init__(self, n_particles=50):
        self.n_particles = n_particles
        self.positions = np.random.rand(n_particles, 2) * 400  # Random positions
        self.velocities = np.zeros((n_particles, 2))  # Initial velocities
        self.temperature = 1.0  # Controls particle motion
        
    def update_solid(self):
        # Increased vibration multiplier from 5 to 10
        original_positions = self.positions.copy()
        vibration = (np.random.rand(self.n_particles, 2) - 0.5) * self.temperature * 10
        self.positions += vibration
        # Return to original positions
        self.positions = 0.9 * self.positions + 0.1 * original_positions
        
    def update_liquid(self):
        # Increased velocity multiplier to 2
        self.velocities += (np.random.rand(self.n_particles, 2) - 0.5) * self.temperature * 2
        self.positions += self.velocities
        # Boundary conditions
        self.positions = np.clip(self.positions, 0, 400)
        # Reduced damping for faster movement
        self.velocities *= 0.98
        
    def update_gas(self):
        # Increased velocity multiplier from 2 to 4
        self.velocities += (np.random.rand(self.n_particles, 2) - 0.5) * self.temperature * 4
        self.positions += self.velocities
        # Boundary conditions with bouncing
        for i in range(2):
            mask = self.positions[:, i] < 0
            self.positions[mask, i] = 0
            self.velocities[mask, i] *= -1
            
            mask = self.positions[:, i] > 400
            self.positions[mask, i] = 400
            self.velocities[mask, i] *= -1
