from config import *

def plot_grain(A, B):

    import matplotlib.pyplot as plt
    y_values = A
    x_values = B

    # Output plot
    plt.grid(True, which="both")
    plt.ylim([0, 1])
    plt.xlim([0.01, 10000])
    plt.semilogx(x_values, y_values)
    plt.title('Grain distribution plot')
    plt.xlabel ('Grain size in Micrometers')
    plt.ylabel ('Percent finer by Weight')
    plt.show()
    plt.savefig("graindist.jpg", bbox_inches='tight')
    #plt.savefig("x.png")

