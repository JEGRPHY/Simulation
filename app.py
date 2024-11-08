import streamlit as st
import pygame
import numpy as np
from PIL import Image
import io
from particle_simulation import ParticleSimulation
from datetime import datetime

# Initialize session state for simulation
if 'simulation' not in st.session_state:
    st.session_state['simulation'] = ParticleSimulation()

# Set up the page
st.title('States of Matter Simulation By JEGR JABBAR')

# Add current date and time
current_datetime = datetime.now().strftime("%B %d, %Y %H:%M:%S")
st.write(f"Current Date and Time: **{current_datetime}**")

st.write("""
This simulation demonstrates how particles behave in different states of matter:
- **Solid**: Particles vibrate but maintain fixed positions
- **Liquid**: Particles move freely while staying close together
- **Gas**: Particles move rapidly and spread throughout the space
""")

# Create radio button for state selection
state = st.radio(
    "Select state of matter:",
    ('Solid', 'Liquid', 'Gas')
)

try:
    # Temperature slider
    temperature = st.slider('Temperature', 0.1, 2.0, 1.0, 0.1)
    
    # Ensure simulation exists
    if 'simulation' not in st.session_state:
        st.session_state['simulation'] = ParticleSimulation()
    
    st.session_state['simulation'].temperature = temperature

    # Initialize Pygame surface
    surface = pygame.Surface((400, 400))

    # Update simulation based on selected state
    if state == 'Solid':
        st.session_state['simulation'].update_solid()
    elif state == 'Liquid':
        st.session_state['simulation'].update_liquid()
    else:  # Gas
        st.session_state['simulation'].update_gas()

    # Draw particles
    surface.fill((255, 255, 255))  # White background
    positions = st.session_state['simulation'].get_positions()
    for pos in positions:
        pygame.draw.circle(surface, (0, 0, 255), pos, 5)

    # Convert Pygame surface to image
    string_image = pygame.image.tostring(surface, 'RGB')
    pil_image = Image.frombytes('RGB', (400, 400), string_image)

    # Display the simulation
    st.image(pil_image, caption=f'Particle behavior in {state} state', use_column_width=True)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    # Reset simulation
    st.session_state['simulation'] = ParticleSimulation()
