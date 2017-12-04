import numpy as np
import matplotlib.pyplot as plt
from IPython import embed

if __name__ == "__main__":

    # Load the data:
    data = np.loadtxt("data/ex1.dat")
    X = data[:, 0]
    y = data[:, 1]

    # Plot the data:
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    plt.show()

    # Start IPython terminal to examine data interactively:
    embed()

