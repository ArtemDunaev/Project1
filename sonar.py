import numpy as np
import common

class Sonar(common.Common):


    def get_coordinates(self, signalleft, signalright):
        spectrumleft = np.fft.fft(signalleft)
        spectrumright = np.fft.fft(signalright)


        n = spectrumleft.size
        spectrumleft[int(n/2):] = 0
        signalleft = np.fft.ifft(spectrumleft)
        spectrumright[int(n / 2):] = 0
        signalright = np.fft.ifft(spectrumright)


        phileft = np.angle(signalleft)
        phiright = np.angle(signalright)
        deltaphi = phiright - phileft
        deltaphi[np.where(deltaphi < -np.pi)] += 2 * np.pi
        deltaphi[np.where(deltaphi > np.pi)] -= 2 * np.pi
        mean_deltaphi = sum(deltaphi) / deltaphi.size
        print("Middle phase = ", mean_deltaphi)
        peleng = np.arcsin((self.c * mean_deltaphi) / (2 * np.pi * self.fs * self.d))
        print("End angle = ", peleng * (180 / np.pi))