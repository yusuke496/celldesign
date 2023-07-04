import numpy as np
#from scipy import integrate
#import scipy
import matplotlib.pyplot as plt
import math
#from sympy.plotting import plot_parametric
#from sympy import var, cos, sin, floor
import warnings
warnings.filterwarnings('ignore')

def fx(t,theta):
    return -2*np.cos(theta)*(np.floor(((np.cos(theta)*t) % 2))-0.5)
def fy(t,theta):
    return -2*np.sin(theta)*(np.floor(((np.sin(theta)*t) % 2))-0.5)
#def gx(t,theta):
    return integrate.quad(lambda t, theta: -2*np.cos(theta)*(np.floor(((np.cos(theta)*t) % 2))-0.5), 0, t ,args=theta)[0]
    #return integrate.quad(lambda x: fx(x,theta), 0, x)[0]
#def gy(t,theta):
    return integrate.quad(lambda t, theta: -2*np.sin(theta)*(np.floor(((np.sin(theta)*t) % 2))-0.5), 0, t ,args=theta)[0]
    #return integrate.quad(lambda x: fy(x,theta), 0, x)[0]
def px(t,theta,n):
    return (-1)**n*np.cos(theta)*t-(-1)**n*(n+1/2)+1/2
def py(t,theta,n):
    return (-1)**n*np.sin(theta)*t-(-1)**n*(n+1/2)+1/2

ini=0
fin=10
d=0.01
nmax=50

s=int((fin-ini)/d)
tilt=1/15
theta=np.arctan(tilt)
t = np.arange(ini,fin,d)
#gx=np.vectorize(gx)
#gy=np.vectorize(gy)
#plt.figure(1)
plt.ylim(-1.1,1.1)
plt.xlim(0,nmax)
#plt.plot(t,fx(t,theta), color='blue')
#plt.plot(t,fy(t,theta), color='red')
#plt.figure(2)
plt.ylim(0,1.1)
plt.xlim(0,nmax)
#plt.plot(t,gx(t,theta),gy(t,theta))
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
#plt.figure(3)
plt.ylim(-0.1,1.1)
plt.xlim(-0.1,1.1)
plt.axis('equal')
#plt.gca().set_aspect('equal', adjustable='box')
plt.hlines(y=[0,1], xmin=0, xmax=1, colors='black', linestyles='solid', linewidths=4)
plt.vlines(x=[0,1], ymin=0, ymax=1, colors='black', linestyles='solid', linewidths=4)
#plt.plot(gx(t,theta),gy(t,theta))
for i in range(len(vecpx)):
    plt.scatter(vecpx[i],vecpy[i] ,color="green", marker='.', s=1)
#plt.plot(t,f(t))
#plt.plot(np.cos(t),np.sin(t))
plt.show()
