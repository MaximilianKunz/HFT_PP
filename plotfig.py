from config import *

def plot_grain(A, B):

    import matplotlib.pyplot as plt
    y_values = A
    x_values = B

    # Output plot
    plt.style.use("seaborn")
    plt.grid(True, which="both")
    plt.ylim([0, 1])
    plt.xlim([0.01, 10000])
    plt.semilogx(x_values, y_values, color='k')
    plt.title('Grain distribution plot')
    plt.xlabel ('Grain size in Milemeters')
    plt.ylabel ('Percent finer by Weight')
    plt.show()
    plt.savefig('graindist.jpg', bbox_inches='tight')
    #plt.savefig("x.png")

def plot_d50 (C):
    import matplotlib.pyplot as plt
    y_values = C["Mean diameter"]
    x_values = C["Time (seconds)"]
    plt.grid(True, which="both")
    plt.plot(x_values, y_values, color='k')
    plt.title('Mean Diameter vs time')
    plt.xlabel('Time in seconds')
    plt.ylabel('Mean diameter')
    plt.show()

#class interact_plot:
#    import mpl_interactions.ipyplot as iplt
 #   import matplotlib.pyplot as plt
#
 #   x_values = B

  #  def f1(df1, idNode, timestep):
   #     array = df1[df1["Node ID"] == idNode]
    #    subarray = array.iloc[timestep, 13:21]
     #   return subarray

  #  fig, ax = plt.subplots()
  #  controls = iplt.plot(x, f1, idNode=(1,10,100), timestep=(1, 10, 100), label="f1")
  #  #iplt.plot(x, f2, controls=controls, label="f2")
  #  _ = plt.legend()
  #  plt.show()

