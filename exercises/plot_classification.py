import numpy as np
import matplotlib.pyplot as plt
from IPython import embed

if __name__ == "__main__":

    # Load the data:
    data = np.loadtxt("data/ex4.dat")
    X = data[:, :-1]
    y = data[:, 2].astype(int)

    # Plot the data:
    fig, ax = plt.subplots()
    ax.scatter(X[:,0], X[:,1], c=['C' + str(i) for i in y])
    plt.show()

    # Start IPython terminal to examine data interactively:
    embed()


