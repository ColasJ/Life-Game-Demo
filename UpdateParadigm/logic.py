import numpy as np
from scipy.stats import norm

ROWS = 100
COLS = 100

# On utilise ici une distribution normale. 
# Définition des paramètres de la distribution normale
mu = 0.4  # Moyenne
sigma = 0.15  # Écart-type

def getLife (x) : 
    return norm.pdf(x, mu, sigma)


# Fonction pour mettre à jour la grille selon les règles du jeu de la vie
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(ROWS):
        for j in range(COLS):
            # Compter la moyenne de vie des voisins
            neighbors_sum = np.sum(grid[max(0, i-1):min(ROWS, i+2), max(0, j-1):min(COLS, j+2)]) - grid[i, j]
            neighbors_num = (min(ROWS, i+2) - max(0, i-1)) * (min(COLS, j+2) - max(0, j-1))
            neighbors_average = neighbors_sum / neighbors_num
            # Appliquer la règle de vie
            new_grid[i, j] = getLife(neighbors_average)
    return new_grid

# Fonction pour initialiser la grille aléatoirement
def init_grid():
    return np.random.rand(ROWS, COLS)