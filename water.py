import numpy as np
import turtle as t
import common


class Water(common.Common):
    def get_signals(self,r,phi):
        time = np.arange(0, self.Tc,1/self.fd)
        signalLeft = np.random.randn(time.size)/10
        signalRight = np.random.randn(time.size) / 10

        delay = r/1500
        dt = self.d/1500*np.sin(phi/180.0*np.pi)
        for i in range(time.size):
            if time[i] > delay and time[i] < delay+self.ti:
                signalLeft[i] += np.sin(2*np.pi*self.fs*time[i])
                signalRight[i] += np.sin(2 * np.pi * self.fs * time[i]-dt)
        return((time, signalLeft, signalRight))
