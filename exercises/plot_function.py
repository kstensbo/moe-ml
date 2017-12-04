import numpy as np
import matplotlib.pyplot as plt
from IPython import embed

if __name__ == "__main__":

    # Load data:
    data = np.loadtxt("data/ex1.dat")
    X = data[:, 0]
    y = data[:, 1]

    # Compute function
    Xf = np.linspace(0, 10, 200)        # x-values to compute function values at
    yf = 0.1 * Xf**2 - 0.5*Xf + 0.3     # y-values

    # Plot the data:
    fig, ax = plt.subplots()
    ax.scatter(X, y)
    ax.plot(Xf, yf, linestyle="-", marker="", color='C1')
    plt.show()

    # Start IPython terminal to examine data interactively:
    embed()

