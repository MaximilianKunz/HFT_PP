import numpy as np


def plot_grain(plot_transform):

    import matplotlib.pyplot as plt
    import matplotlib.font_manager as font_manager
    # set font properties
    hfont = {'family': 'normal',
             'weight': 'normal',
             'size': 10,
             'style': 'normal',
             'fontname': 'Arial'}
    font = font_manager.FontProperties(family=hfont['fontname'],
                                       weight=hfont['weight'],
                                       style=hfont['style'],
                                       size=hfont['size'])
    # create plot
    y_values = list(range(1, plot_transform.size + 1))
    #x_values = lit_fractions
    fig = plt.figure(figsize=(6, 3), dpi=150, facecolor='w', edgecolor='k')
    axe = fig.add_subplot(1, 1, 1)
    axe.plot(y_values, plot_transform, linestyle='-', color="slategrey", label='percentage')

    # Define axis labels and legend
    axe.set_xlabel("particle diameter (mm)", **hfont)
    axe.set_ylabel("Percent (%)", **hfont)
    axe.legend(loc='upper left', prop=font, facecolor='w', edgecolor='gray', framealpha=1, fancybox=0)

    # Set grid
    axe.grid(color='gray', linestyle='-', linewidth=0.2)
    axe.set_ylim((0, int(np.nanmax(plot_transform) * 1.1)))
    axe.set_xlim((0, plot_transform + 1))

    # Output plot
    plt.savefig("graindist.png", bbox_inches='tight')
    plt.show()
