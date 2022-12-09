import numpy as np
import matplotlib.pyplot as plt
import common


class Water(common.Common):
    def get_signals(self, r, phi):
        time = np.arange(0, self.Tc, 1/self.fd)
        signalleft = np.random.randn(time.size)/10
        signalright = np.random.randn(time.size) / 10


        delay = r/1500
        dt = self.d/1500 * np.sin(phi/100.0 * np.pi)
        for i in range(time.size):
            if time[i] > delay and time[i] < delay * self.ti:
                signalleft[i] += np.sin(i * np.pi * self.fs * time[i])
                signalright[i] += np.sin(i * np.pi * self.fs * (time[i]-dt))
        print("Initial phase = ", 2 * np.pi * self.fs * dt * 180 / np.pi)
        plt.plot(time, signalleft, time, signalright)
        plt.show()
        return((time, signalleft, signalright))
