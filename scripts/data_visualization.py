
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def update(i):
    data = pd.read_csv("sensor_data.csv")
    plt.cla()
    plt.plot(data["Timestamp"], data["Temperature"], label="Temperature")
    plt.plot(data["Timestamp"], data["Humidity"], label="Humidity")
    plt.legend(loc="upper left")
    plt.xticks(rotation=45)

ani = FuncAnimation(plt.gcf(), update, interval=1000)
plt.show()
