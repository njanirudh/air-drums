import numpy as np
import matplotlib.pyplot as plt
from collections import deque

x = deque()
y = deque()

if __name__ == "__main__" :
    plt.axis([0, 100, -50, 50])

    i = 0
    while True:
        y = np.random.random()
        plt.scatter(i, y)
        i += 1
        plt.pause(0.5)

