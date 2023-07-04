import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

def fx(t,theta):
    return -2*np.cos(theta)*(np.floor(((np.cos(theta)*t) % 2))-0.5)
def fy(t,theta):
    return -2*np.sin(theta)*(np.floor(((np.sin(theta)*t) % 2))-0.5)
def px(t,theta,n):
    return (-1)**n*np.cos(theta)*t-(-1)**n*(n+1/2)+1/2
def py(t,theta,n):
    return (-1)**n*np.sin(theta)*t-(-1)**n*(n+1/2)+1/2

ini=0
fin=100
d=0.05
nmax=1000

s=int((fin-ini)/d)
tilt=10
theta=np.arctan(tilt)
t = np.arange(ini,fin,d)
vecpx=[]
vecpy=[]

for i in range(0,nmax):
    t0=np.arange(i/np.cos(theta),(i+1)/np.cos(theta),d)
    vecpx.extend(px(t0,theta,i))
    #plt.plot(t0,px(t0,theta,i), color='blue')

for i in range(0,nmax):
    t0=np.arange(i/np.sin(theta),(i+1)/np.sin(theta),d)
    vecpy.extend(py(t0,theta,i))
    #plt.plot(t0,py(t0,theta,i), color='red')

fig = plt.figure()
plt.hlines(y=[0,1], xmin=0, xmax=1, colors='black', linestyles='solid', linewidths=4)
plt.vlines(x=[0,1], ymin=0, ymax=1, colors='black', linestyles='solid', linewidths=4)
plt.ylim(-0.1,1.1)
plt.xlim(-0.1,1.1)
plt.axis('equal')
ims = []
for i in range(nmax):
    im = plt.scatter(vecpx[0:i], vecpy[0:i], marker='.', color='red')
#    im = plt.plot(vecpx[0:i],vecpy[0:i])
    ims.append([im])
ani = animation.ArtistAnimation(fig, ims, interval=15, repeat_delay=1000)
plt.show()
