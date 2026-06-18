import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Simple2DHarmonicOscillator import xarray, T

fig,ax = plt.subplots(figsize = (5,5) )

PositionPoint = ax.scatter(*xarray[0]) # Scatter graph showing the location of the body at a given time

Tail = ax.plot(*xarray[0])[0] # Small tail which follows the oscillator for a given number of frames


# Animation parameters
TailLength = 10 # length of tail in frames
Interval = 30 # Interval between frames in milliseconds
Period = 30 * T # Period of oscillation in milliseconds

xarrayForTail = np.concatenate((xarray[-TailLength:], xarray)) # xarray with incontinuity removed for tail

def Update(frame : int):
    NewPoint = xarray[frame]
    TailPoints = xarrayForTail[frame : frame + TailLength]
    PositionPoint.set_offsets(NewPoint)
    Tail.set_data(TailPoints.transpose())

    return (PositionPoint,Tail)

ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

ax.set_title(f'2D Isotropic Harmonic Oscillator \n Period: {round(Period / 1000,3)} $s$')

ani = animation.FuncAnimation(fig = fig, func = Update, frames = len(xarray),interval = Interval)
ani.save('2DIsotropicHarmonicOscillator.gif')
plt.show()
