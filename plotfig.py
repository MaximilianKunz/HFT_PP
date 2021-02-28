from config import *

def plot_grain(A, B):
    """
    Plots the grain distribution for an specific Node and time.
    :param array_1d: A (the weight of the each fraction) / Variable according the Node and time
    :param array_1d: B (list of diameters for each of defined fractions) / Uniform for the whole simulation
    :return: show and save plot in script directory as graindist.png
    """

    import matplotlib.pyplot as plt
    y_values = A
    x_values = B

    # Output plot
    plt.grid(True, which="both")
    plt.ylim([0, 1])
    plt.xlim([1, 1000])
    plt.semilogx(x_values, y_values, color='k')
    plt.title('Grain distribution plot')
    plt.xlabel ('Grain size in Milemeters')
    plt.ylabel ('Percent finer by Weight')
    plt.show()
    plt.savefig('graindist.png', bbox_inches='tight')

def plot_d50 (C):
    """
    Plots the mean diameter along the simulation time for an specific Node
    :param array_2d: C (array with resultant mean diameter and the simulation time) / Variable according the Node
    :return: show and save plot in script directory as plotd50.png
    """
    import matplotlib.pyplot as plt
    plt.style.use("seaborn")
    y_values = C["Mean diameter"]
    x_values = C["Time (seconds)"]
    plt.grid(True, which="both")
    plt.plot(x_values, y_values, color='k')
    plt.title('Mean Diameter vs time')
    plt.xlabel('Time in seconds')
    plt.ylabel('Mean diameter')
    plt.show()
    plt.savefig('plotd50.jpg', bbox_inches='tight')


