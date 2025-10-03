import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    """Configura os elementos visuais do gráfico."""
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(titulo)

def r1(x):
    return (18 - 3 * x) / 2

def objetiva(x, y):
    return 3000 * x + 2000 * y

def plotar_restricoes(x):
    plt.plot(x, r1(x), label='3x + 2y <= 18', color='blue')
    plt.axvline(x=5, label='x <= 5', color='green', linestyle='--')
    plt.axvline(x=2, label='x >= 2', color='orange', linestyle='--')
    plt.axhline(y=6, label='y <= 6', color='purple', linestyle='--')

def gradiente():
    plt.arrow(0, 0, 3, 2, head_width=0.2, head_length=0.2, fc='red', ec='red', label='Gradiente')

def area_factibilidade(x):
    limite_superior = np.minimum(r1(x), 6)
    limite_inferior = np.zeros_like(x)

    plt.fill_between(
        x,
        limite_inferior,
        limite_superior,
        where=((x >= 2) & (x <= 5)),
        color='gray',
        alpha=0.5,
        label='Área de Factibilidade'
    )

def curvas_nivel(xmax, ymax):
    x_grid = np.arange(0, xmax + 0.5, 0.5)
    y_grid = np.arange(0, ymax + 0.5, 0.5)
    x, y = np.meshgrid(x_grid, y_grid)
    z = objetiva(x, y)
    contour = plt.contour(x, y, z, levels=10, colors='k', linestyles='--', linewidths=0.8)
    plt.clabel(contour, inline=True, fontsize=8)

def main():
    xmax = 8
    ymax = 8
    x = np.linspace(0, xmax, 400)

    plt.figure(figsize=(8, 8))

    plotar_restricoes(x)
    area_factibilidade(x)
    gradiente()
    curvas_nivel(xmax, ymax)
    plot('Exercício 02: Max(z) = 3000x + 2000y', xmax, ymax) 
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()