import matplotlib.pyplot as plt
from collections import deque

graph_data = open('/home/anirudh/NJ/Github/air-drums/midi-player/accelerometer.txt', 'r').read()

xs,ys,zs = deque([]),deque([]),deque([])

path = "accelerometer.txt"
with open(path) as fp:
    for line in fp:
        plt.axis([0, 20, -60, 60])

        single = line.split(",")

        # ---------------------------------
        x_val = round(float(single[0]),2)
        xs.appendleft(x_val)

        # ---------------------------------
        y_val = round(float(single[1]),2)
        ys.appendleft(y_val)

        # ---------------------------------
        z_val = round(float(single[2]),2)
        zs.appendleft(z_val)

        # ---------------------------------

        plt.plot([i for i in range(0,len(xs))],xs,c='r')
        plt.plot([i for i in range(0,len(ys))],ys,c='g')
        plt.plot([i for i in range(0,len(zs))],zs,c='b')

        if len(xs) == 20:
            xs.pop()
            ys.pop()
            zs.pop()

        plt.pause(0.1)
        plt.clf()
#plt.show()
