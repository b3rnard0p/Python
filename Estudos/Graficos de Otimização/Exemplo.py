import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    plt.xlim(0, xmax)
    plt.ylim(0, ymax)

    plt.xlabel('X')
    plt.ylabel('Y')

    plt.legend()

    plt.title(titulo)

def y1(x):  
    return 25 - 0.5 * x

def y2(x):
    return 40 - (4/3) * x

def objetiva(x, y):
    return 1000*x + 50*y

def plot_restricoes(x):
    plt.plot(x, y1(x), label='2x + 4y = 100', color='blue')
    plt.plot(x, y2(x), label='4x + 3y = 120', color='orange')

def gradiente():
    plt.arrow(0,0,6,10, head_width=1, head_length=1, fc='red', ec='red', label='Gradiente')

def area_factbilidade(x):
    y_feasible = np.minimum(y1(x), y2(x))

    plt.fill_between(
        x, 
        0, 
        y_feasible, 
        where=(y_feasible >= 0), 
        color='gray', 
        alpha=0.5, 
        label='Área de Factibilidade'
    )

def curvas_nivel(xmax, ymax):
    x_grid = np.arange(0, xmax + 1, 1)
    y_grid = np.arange(0, ymax + 1, 1)

    x, y = np.meshgrid(x_grid, y_grid)

    z = objetiva(x, y)

    contour = plt.contour(x, y, z, levels=40, colors='k', linestyle='--', linewidths=1.2)
    plt.clabel(contour, inline=True, fontsize=8)

def main():
    xmax = 60
    ymax = 60

    x = np.linspace(0, xmax, 400)

    plt.figure(figsize=(6, 6))

    plot_restricoes(x)
    plot('Grafico Linear', xmax, ymax)
    gradiente()
    area_factbilidade(x)
    curvas_nivel(xmax, ymax)

    plt.show()

if __name__ == "__main__":
    main()