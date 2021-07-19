#!/usr/bin/python
import numpy as np                                                              
from matplotlib import pyplot as plt                                            
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import animation
plt.rcParams['animation.ffmpeg_path'] = '/opt/local/bin/ffmpeg'

#Construct Figure and Plot Data
#fig = figure("MyFigure",figsize=(5,5))
#fig = plt.figure(figsize=(16,10))
#fig, (ax1, ax2) = plt.subplots(2,1,figsize=(16,10))
fig, (ax1,ax2) = plt.subplots(nrows=2,sharex=True)
ax1.set_xlim([0, 0.5])
ax2.set_xlim([0, 0.5])
ax1.set_ylim([-2, 2])
ax2.set_ylim([-3, 3])
ax1.title.set_text('String plucked at one sixth of the length')
ax2.title.set_text('String plucked at the mid-point')
#ax = plt.axes(xlim = (0,0.5),ylim=(-2,2))
#ax2 = plt.axes(xlim = (0,0.5),ylim=(-2,2))
line0, = ax1.plot([], [], lw=2)
line1, = ax1.plot([], [], lw=2)
line2, = ax1.plot([], [], lw=2)
line3, = ax1.plot([], [], lw=2)
line4, = ax1.plot([], [], lw=2)
line5, = ax1.plot([], [], lw=2)
line6, = ax1.plot([], [], lw=5)
line7, = ax2.plot([], [], lw=2)
line8, = ax2.plot([], [], lw=2)
line9, = ax2.plot([], [], lw=2)
line10, = ax2.plot([], [], lw=2)
line11, = ax2.plot([], [], lw=2)
line12, = ax2.plot([], [], lw=2)
line13, = ax2.plot([], [], lw=5)
# Define the init function, which draws the first frame (empty, in this case)
def init():
    for i in np.arange(0,13,1):
        globals()['line'+str(i)].set_data([], [])
    return (line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13)  

# Animate draws the i-th frame, where i starts at i=0 as in Python.
def animate(i):
    x = np.linspace(0, 0.5, 2000)
    for j in np.arange(1,19,1):
        globals()['z'+str(j)]= 20/(j*np.pi)**2*np.sin(j*np.pi/6)*np.sin(2*j*np.pi*(x))*np.cos(j* np.pi * (0.01*i))
    sum=0
    for j in np.arange(1,19,1):
        sum+=globals()['z'+str(j)]
    globals()['z'+str(19)]=sum
    for j in np.arange(0,6,1):
        globals()['line'+str(j)].set_data(x,globals()['z'+str(j+1)])
    line6.set_data(x,z19)

    for j in np.arange(1,19,1):
        globals()['z'+str(j)]= 20/(j*np.pi)**2*np.sin(j*np.pi/2)*np.sin(2*j*np.pi*(x))*np.cos(j* np.pi * (0.01*i))
    sum=0
    for j in np.arange(1,19,1):
        sum+=globals()['z'+str(j)]
    globals()['z'+str(20)]=sum
    for j in np.arange(7,14,1):
        globals()['line'+str(j)].set_data(x,globals()['z'+str(j+1-7)])
    line13.set_data(x,z20)

    return (line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13)  
    #return (line0,line1,line2,line3,line4,line5,line6)


# Create the animation object by calling the Python function FuncAnimaton
anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20,blit=True)
#anim.save('guitarsubplot.mp4', writer=PillowWriter(fps=30))
FFwriter = animation.FFMpegWriter()
anim.save('basic_animation.mp4', writer = FFwriter, fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()
