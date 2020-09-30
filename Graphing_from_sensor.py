import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import read_sensor
import time
"""



x = read_sensor.X
y = read_sensor.Y
z = read_sensor.Z



quiver = ax.quiver(0,0,0,read_sensor.rotation_x,read_sensor.rotation_y(),read_sensor.rotation_z()) # * passes get_arrows as tuple
#print(read_sensor.X,read_sensor.Y,read_sensor.Z) #this is correct


    
#animation call
    


"""

#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

fig, ax = plt.subplots(subplot_kw=dict(projection="3d"))

def get_arrow(i): # get arrow with theta
    u = 0
    v = 0
    w = 0
    x = read_sensor.rotation_x()
    y = read_sensor.rotation_y()
    z = read_sensor.rotation_z()
    
    return u,v,w,x,y,z

quiver = ax.quiver(*get_arrow(0), length=1, normalize=True)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


def update(i):
    
    global quiver
    quiver.remove()
    #print(*get_arrow(i))
    time.sleep(1)
    quiver = ax.quiver(*get_arrow(i), length=1, normalize=True)
   
ani = FuncAnimation(fig, update, range(1000), interval=1. /30.)
plt.show()

#ani.save('animation.mp4',writer=writer)