from config import *

def plot_grain(A, B):

    import matplotlib.pyplot as plt
    y_values = A
    x_values = B

    # Output plot
    plt.grid(True, which="both")
    plt.ylim([0, 1])
    plt.xlim([0.01, 10000])
    plt.semilogx(x_values, y_values, color='k')
    plt.title('Grain distribution plot')
    plt.xlabel ('Grain size in Micrometers')
    plt.ylabel ('Percent finer by Weight')
    plt.show()
    plt.savefig("graindist.jpg", bbox_inches='tight')
    #plt.savefig("x.png")

def plot_d50 (C, D):
    import matplotlib.pyplot as plt
    y_values = C
    x_values = D

    plt.grid(True, which="both")
    plt.plot(x_values, y_values, color='k')
    plt.title('Mean Diameter vs time')
    plt.xlabel('Time in seconds')
    plt.ylabel('Mean diameter')
    plt.show()

#class interactplot:

#    def f1(id_node, transformed_data):
#       return np.sin(x * tau) * x * beta

#    def plot_d50_interactive(C, D):
#        import mpl_interactions.ipyplot as iplt
#        import matplotlib.pyplot as plt
#        import numpy as np

#        x = np.linspace(0, np.pi, 100)

#        fig, ax = plt.subplots()
#        controls = iplt.plot(x, f1, tau=tau, beta=(1, 10, 100), label="f1")
#        iplt.plot(x, f2, controls=controls, label="f2")
#    _ = plt.legend()
#        plt.show()