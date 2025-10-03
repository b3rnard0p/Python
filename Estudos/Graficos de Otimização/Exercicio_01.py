import numpy as np
import matplotlib.pyplot as plt

def plot(titulo, xmax, ymax):
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.xlim(0, xmax)
    plt.ylim(0, ymax)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title(titulo)

def r1(x1):
    return 200 - x1

def objetiva(x1, x2):
    return 0.15 * x1 + 0.6 * x2

def plotar_restricoes(x1):
    plt.plot(x1, r1(x1), label='x1 + x2 <= 200', color='blue')
    plt.axvline(x=120, label='x1 <= 120', color='green', linestyle='--')
    plt.axhline(y=40, label='x2 >= 40', color='purple', linestyle='--')

def gradiente():
    plt.arrow(0, 0, 0.15 * 50, 0.6 * 50, head_width=5, head_length=5, fc='red', ec='red', label='Gradiente')

def area_factibilidade(x1):
    limite_inferior = np.full_like(x1, 40)
    limite_superior = r1(x1)

    plt.fill_between(
        x1,
        limite_inferior,
        limite_superior,
        where=((x1 <= 120) & (limite_superior >= limite_inferior)),
        color='gray',
        alpha=0.5,
        label='Área de Factibilidade'
    )

def curvas_nivel(xmax, ymax):
    x_grid = np.arange(0, xmax + 1, 1)
    y_grid = np.arange(0, ymax + 1, 1)
    x1, x2 = np.meshgrid(x_grid, y_grid)
    z = objetiva(x1, x2)
    contour = plt.contour(x1, x2, z, levels=15, colors='k', linestyles='--', linewidths=0.8)
    plt.clabel(contour, inline=True, fontsize=8)

def main():
    xmax = 150
    ymax = 220
    x1 = np.linspace(0, xmax, 400)

    plt.figure(figsize=(8, 8))
    
    plotar_restricoes(x1)
    area_factibilidade(x1)
    gradiente()
    curvas_nivel(xmax, ymax)
    plot('Exercício 01: Max(z) = 0.15x1 + 0.6x2', xmax, ymax)
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()