import numpy as np

ROWS = 100
COLS = 100

# Fonction pour mettre à jour la grille selon les règles du jeu de la vie
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            # Compter le nombre de voisins vivants
            neighbors_sum = np.sum(grid[max(0, i-1):min(ROWS, i+2), max(0, j-1):min(COLS, j+2)]) - grid[i, j]
            # Appliquer les règles
            if grid[i, j] == 1:
                if neighbors_sum < 2 or neighbors_sum > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors_sum == 2 or neighbors_sum == 3:
                    new_grid[i, j] = 1
    return new_grid

# Fonction pour initialiser la grille aléatoirement
def init_grid():
    return np.random.choice([0, 1], size=(ROWS, COLS), p=[0.7, 0.3])

