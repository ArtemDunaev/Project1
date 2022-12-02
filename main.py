import matplotlib as matplotlib
import tikzplotlib as tikzplotlib
import water
import sonar
import plotter

water = water.Water()
(time, signalLeft, signalRight) = water.get_signals(800, 30)

plotter = plotter.Plotter(400, 400)

distance = sonar.Sonar().get_coordinates(signalLeft, signalRight)
