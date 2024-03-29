from UpdateParadigm.logic import init_grid, update_grid
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Fonction pour animer la grille
def animate(frame, img, grid):
    new_grid = update_grid(grid)
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# Initialisation de la grille
grid = init_grid()

# Initialisation de l'affichage
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, animate, fargs=(img, grid), frames=100, interval=100)
plt.show()

