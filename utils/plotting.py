import matplotlib.pyplot as plt

def plot_basic(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    return fig
