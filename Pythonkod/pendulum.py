# Python simulation of 2D pendulum motion with real time animation
# Last updated 2019-02-20

# Importing necessary  modules
import sys
from math import *
import matplotlib.pyplot as plt
from matplotlib import animation
import studentSol_withSolution

#import studentSol

#Commandline argument

try:
    arg = sys.argv[1]
except:
    raise Exception('exit')

# Defining variables
t = 0  # initial time
tmax = 30  # final time
try:
	dt = float(sys.argv[2])  # time step
except:
	dt = 0.03


theta = pi/2  # initial position
energy_for_point = 0


dtheta = 0.0  # initial velocity
g = 9.8  # gravitational acceleration
m = 1  # mass of the pendulum
c = 9  # c=g/L = 9
L = g / c  #  length of the pendulum

gama = 1 # coefficient of the damping term (in the damped pendulum)

time = []  # list to store time 
pos = []  # list to store angular position
vel = []  # list to store angular velocity
energy = []  # list to store energy

stepsperframe = 3
try:
    numframes = int(tmax / (stepsperframe * dt))
except:
    raise Exception('exit')
    
def handle_close(evt):
     # Plotting position, velocity and energy (vs. time)
    fig2 = plt.figure()
    plt.plot(time, pos, label = 'Position')
    plt.plot(time, vel, label = 'Velocity')
    plt.plot(time, energy, label = 'Energy')
    plt.legend(loc = 'upper left')
    plt.xlabel('Time')
    plt.ylabel('Energy, position and velocity')
    plt.grid()

# Creating a 1.2 * 1.2 window, for the animation of the pendulum motion
plt.rcParams['toolbar'] = 'None'
fig = plt.figure(figsize=(5,5))
ax = plt.subplot(xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(50, 250, 500, 500)
fig.canvas.mpl_connect('close_event', handle_close)


plt.axhline(y=0)  # draw a default horizontal line at y=0 that spans the x-range
plt.axvline(x=0)  # draw a default horizontal line at x=0 that spans the y-range
pendulum_line, = ax.plot([], [], lw=5) # preparing to plot the pendulum after creation of it.

def dtInterval(arg):
    try:
        dt = float(arg[2])
        if isinstance(dt, float) and dt <= 0.05 and dt >= 0.001:
            return True
        else:
            return False
    except:
        return False
    
def intervalFunction(numframes):
    inter = 1020-numframes
    if inter <= 0:
        return 10
    else:
        return inter
    


# Perform a single integration step
###################################################################################################################

def numerical_method():
    ''' The numerical_method function solve the non linear differential equation for pendulum motion by implementing numerical methods'''
    global t, theta, dtheta, energy_for_point
    if arg == "euler":
        t, theta, dtheta = studentSol_withSolution.euler(t, theta, dtheta, dt, m, L, g)
        energy_for_point = studentSol_withSolution.energy(theta, dtheta, m, L, g)
        #t, theta, dtheta = studentSol.euler(t, theta, dtheta, dt, m, L, g)
        #energy_for_point = studentSol.energy(theta, dtheta, m, L, g)

    elif arg == "eulerCromer":
        t, theta, dtheta = studentSol_withSolution.eulerCromer(t, theta, dtheta, dt, m, L, g)
        energy_for_point = studentSol_withSolution.energy(theta, dtheta, m, L, g)
		#t, theta, dtheta = studentSol.eulerCromer(t, theta, dtheta, dt, m, L, g)
        #energy_for_point = studentSol.energy(theta, dtheta, m, L, g)



    time.append(t) # Adding the time value to the time-list
    pos.append(theta) # Adding the position value to the position-list
    vel.append(dtheta) # Adding the velocity value to the velocity-list
    energy.append(energy_for_point)  # Energy of the pendulum

###################################################################################################################

def init():
    pendulum_line.set_data([0, sin(pi/2)], [0, -cos(pi/2)])
    return pendulum_line,

# Animation function which integrates a few steps and return a line for the pendulum
def animate(framenr):
    for it in range(stepsperframe):
        numerical_method()

    #x and y defines points in between which the line for the pendulum is drawn for each frame
    x = [0, sin(theta)]
    y = [0, -cos(theta)]
    pendulum_line.set_data(x, y)
    return pendulum_line,


# Call the animator, blit=True means only re-draw parts that have changed
#print(len(sys.argv) == 2, len(sys.argv) == 3, dtInterval(sys.argv), arg == "euler", arg == "eulerCromer")
if (len(sys.argv) == 2  or ((len(sys.argv) == 3) and dtInterval(sys.argv))) and (arg == "euler" or arg == "eulerCromer"):
    anim = animation.FuncAnimation(fig, animate, frames=numframes, init_func=init, interval=intervalFunction(numframes), blit=True, repeat=False)
    plt.show()
    
elif len(sys.argv) == 2:
    print("No valid argument. Write 'euler' or 'eulerCromer' in main.py")
    
elif arg != "euler" and arg != "eulerCromer":
    print("No valid argument. Write 'euler' or 'eulerCromer' in main.py")

elif len(sys.argv) == 3:
    print("Invalid argument for step size. Follow instructions in main.py")

elif len(sys.argv) > 3:
    print("No valid argument. Write 'euler' or 'eulerCromer' in main.py")

else: 
    print("Now even I don't know what you did wrong")

    


