import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Interactive Wireframe Sphere")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Parameters for the wireframe sphere
radius = 150
num_segments = 30
rotation_speed = 0.005

# Function to project 3D coordinates to 2D screen coordinates
def project(point):
    x, y, z = point
    scale = 500 / (z + 500)
    x = width // 2 + int(x * scale)
    y = height // 2 - int(y * scale)
    return x, y

# Generate points for the wireframe sphere
points = []
for i in range(num_segments):
    theta = 2 * math.pi * i / num_segments
    for j in range(num_segments):
        phi = math.pi * j / num_segments
        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)
        points.append((x, y, z))

# Define edges of the sphere
edges = []
for i in range(num_segments):
    for j in range(num_segments):
        p1 = i * num_segments + j
        p2 = (i + 1) % num_segments * num_segments + j
        p3 = i * num_segments + (j + 1) % num_segments
        edges.extend([(p1, p2), (p1, p3)])

# Main loop
clock = pygame.time.Clock()
angle_x = 0
angle_y = 0
dragging = False
last_mouse_pos = None

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                dragging = True
                last_mouse_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                x1, y1 = last_mouse_pos
                x2, y2 = pygame.mouse.get_pos()
                dx, dy = x2 - x1, y2 - y1
                last_mouse_pos = pygame.mouse.get_pos()
                angle_y += dx * 0.01
                angle_x += dy * 0.01

    # Clear the screen
    screen.fill(WHITE)

    # Rotate the points
    rotated_points = []
    for point in points:
        x, y, z = point
        # Rotate around x-axis
        y_rotated = y * math.cos(angle_x) - z * math.sin(angle_x)
        z_rotated = y * math.sin(angle_x) + z * math.cos(angle_x)
        # Rotate around y-axis
        x_rotated = x * math.cos(angle_y) - z_rotated * math.sin(angle_y)
        z_final = x * math.sin(angle_y) + z_rotated * math.cos(angle_y)
        rotated_points.append((x_rotated, y_rotated, z_final))

    # Project and draw the wireframe sphere
    for edge in edges:
        point1 = rotated_points[edge[0]]
        point2 = rotated_points[edge[1]]
        x1, y1 = project(point1)
        x2, y2 = project(point2)
        pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 1)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()