import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d
import numpy as np


if __name__ == "__main__":

    xs,ys,zs = [],[],[]

    count = 0

    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')

    path = "accelerometer.txt"
    with open(path) as fp:
        for line in fp:
            single = line.split(",")
            # print(single[0])
            x_val = round(float(single[0]),2)
            xs.append(x_val)

            y_val = round(float(single[1]),2)
            ys.append(y_val)

            z_val = round(float(single[2]),2)
            zs.append(z_val)

            count += 1

            print(x_val,y_val,z_val)

    plt.plot([i for i in range(0,count)],xs)
    plt.plot([i for i in range(0,count)],ys)
    plt.plot([i for i in range(0,count)],zs)

    # plt.scatter(xs,ys,zs)

    plt.show()



