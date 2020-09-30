import smbus
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import time
#from mpu6050 import mpu6050
#from best_working_example import*

# Register
#mpu = mpu6050(0x68)
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
"""
accel_data = mpu.get_accel_data() #gets data from mpu
gyro_data = mpu.get_gyro_data()
get_data = mpu.get_all_data()
"""

def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def get_z_rotation(x,y,z):
    radians = math.atan2(z, dist(x,y))
    return math.degrees(radians)

def get_ax(): #x accelerometer data
    accel_data = mpu.get_accel_data() 
    ax = accel_data['x']
    return ax
"""
def get_ay():
    accel_data = mpu.get_accel_data() 
    ay = accel_data['y']
    return ay
    
def get_az():
    accel_data = mpu.get_accel_data() 
    az = accel_data['z']
    return az

def get_gx():
    gyro_data = mpu.get_gyro_data()
    gx = gyro_data['x']
    return gx

def get_gy():
    gyro_data = mpu.get_gyro_data()
    gy = gyro_data['y']
    return gy

def get_gz():
    gyro_data = mpu.get_gyro_data()
    gz = gyro_data['z']
    return gz
""" 


bus = smbus.SMBus(1) 
address = 0x68       

bus.write_byte_data(address, power_mgmt_1, 0)

gyro_xout = read_word_2c(0x43)
gyro_yout = read_word_2c(0x45)
gyro_zout = read_word_2c(0x47)

acceleration_xout = read_word_2c(0x3b)
acceleration_yout = read_word_2c(0x3d)
acceleration_zout = read_word_2c(0x3f)
 
acceleration_xout_scaled = acceleration_xout / 16384.0
acceleration_yout_scaled = acceleration_yout / 16384.0
acceleration_zout_scaled = acceleration_zout / 16384.0


#fig, ax = plt.subplots(subplot_kw=dict(projection="3d")) #fig section
X = get_x_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
Y = get_y_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
Z = get_z_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)

def rotation_x():
    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)
    
    acceleration_xout_scaled = acceleration_xout / 16384.0
    acceleration_yout_scaled = acceleration_yout / 16384.0
    acceleration_zout_scaled = acceleration_zout / 16384.0
    X = get_x_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    return X

def rotation_y():
    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)
 
    acceleration_xout_scaled = acceleration_xout / 16384.0
    acceleration_yout_scaled = acceleration_yout / 16384.0
    acceleration_zout_scaled = acceleration_zout / 16384.0
    Y = get_y_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    return Y

def rotation_z():
    acceleration_xout = read_word_2c(0x3b)
    acceleration_yout = read_word_2c(0x3d)
    acceleration_zout = read_word_2c(0x3f)
 
    acceleration_xout_scaled = acceleration_xout / 16384.0
    acceleration_yout_scaled = acceleration_yout / 16384.0
    acceleration_zout_scaled = acceleration_zout / 16384.0
    Z = get_z_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    return Z

def get_updated_xyz():
    x = get_x_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    y = get_y_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    z = get_z_rotation(acceleration_xout_scaled, acceleration_yout_scaled, acceleration_zout_scaled)
    return x, y, z
"""
for i in range(10):
    
    print(rotation_x(), "", rotation_y(),"",rotation_z())
    time.sleep(1)
"""