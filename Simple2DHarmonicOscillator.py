import numpy as np



# Parameters
xeq = np.zeros(shape = 2) # Equilibrium position
k = 1 # Spring constant
m = 1 # Mass
omega = np.sqrt(k/m) # Orbital frequency 
T = 2 * np.pi / omega # Orbital period

# Initial conditions
ti = 0 # Start time
vi = np.array([np.sqrt(k/m),0]) # Initial velocity
xi = np.array([0,1]) # Initial position
tf = T # End time

# Time points
n = 100 # number of time points


tarray = np.linspace(ti, tf, n) # array of time points

def HarmonicOscillator(tarray : np.ndarray, dim : int = 2):
    xarray = np.zeros(shape = (len(tarray), dim)) # array of coordinates

    for k, t in enumerate(tarray):
        xarray[k] = xeq + (xi - xeq) * np.cos(omega * (t-ti)) + vi / omega * np.sin(omega * (t-ti)) # expression for the position of the oscillator
    
    return xarray

xarray = HarmonicOscillator(tarray)