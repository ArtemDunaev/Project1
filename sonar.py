import numpy as np
import common

class Sonar(common.Common):


    def get_coordinates(self,signalLeft,signalRight):
        spectrumLeft = np.fft.fft(signalLeft)
        spectrumRight = np.fft.fft(signalRight)


        n = spectrumLeft.size
        spectrumLeft[int(n/2):] = 0
        zLeft = np.abs(np.fft.ifft(spectrumLeft))
        sigma = np.sqrt( (np.sum(np.sqrt(zLeft))/n) )
        detection_level = np.where(zLeft>=sigma)
        print(detection_level)
        distance = ((detection_level[0][0])/self.fd) * 1500
        print(distance)
