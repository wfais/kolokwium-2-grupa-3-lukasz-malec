import numpy as np
import matplotlib.pyplot as plt

# Wygeneruj dane (np. 2 tablice x i y o długości 10) za pomocą NumPy.
# Narysuj wykres punktowy (funkcją ax.scatter(...) lub plt.scatter(...)).
# Podpisz osie (np. X axis, Y axis) oraz ustaw tytuł.
# Funkcja ma zwracać obiekt matplotlib.figure.Figure, co ułatwi testy.


def draw_scatter_plot():
    """
    1) Wygeneruj dane x, y (np. np.arange(10) i jakieś y losowe).
    2) Rysuj wykres punktowy (scatter).
    3) Ustaw etykiety osi, tytuł, legendę.
    4) Zwróć obiekt Figure.
    """
    np.random.seed(123)

    
    # utwórz x, y
    x =  np.arange(10)
    y = np.random.rand(10) * 10
    
    # fig, ax = 
    fig, ax = plt.subplots()

    # print(isinstance(fig, plt.Figure)
    
    # ax.scatter( ... )
    ax.scatter(x, y, color='blue', label = "dane punktowe")


    # label dla x, y, title, legend
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_title('Wykres punktowy')
    ax.legend()

    ax.set_xticks(np.arange(0, 12, 1))
    ax.set_yticks(np.arange(0, 13, 1))

    # return rysunek
    return fig

if __name__ == '__main__':
    fig = draw_scatter_plot()
    plt.show()
