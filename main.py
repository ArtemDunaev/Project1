import matplotlib as matplotlib
import tikzplotlib as tikzplotlib
import water
import sonar


water = water.Water()
(time, signalleft, signalright) = water.get_signals(800, 30)
sonar.Sonar().get_coordinates(signalleft, signalright)