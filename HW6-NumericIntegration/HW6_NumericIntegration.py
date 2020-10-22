import numpy as np
import matplotlib.pyplot as plt
#The purpose of this code is to use numeric integration to produce a wavefunction for a harmonic oscillator

#define particle characteristics
m = 1
h = 1

#define starting point of exponential decay of wavefunction in classically forbidden region
x0 = -5
#define the arrays to store the x and y points
x_points = []
wf_points = []

#step size (basically the width of dx)
d = 0.001


#definition of z(x)
def z(x):
    return 2*x

#definiton of Analytical Wavefunction AW(x), which exists in the classicaly forbidden region
def awf(x):
    return np.exp(((-1*2)/3)*(np.sqrt((2*m)/(h*h)))*((-1*x)**(3/2)))

#add the initial three points of the analytical wavefunction to the y array
wf_points.append(awf(x0))
wf_points.append(awf(x0+d))
wf_points.append(awf(x0+2*d))

#add the initial three points of the analytical wavefunction to the x array
x_points.append(x0)
x_points.append(x0+d)
x_points.append(x0+(2*d))

#numeric integration of the wavefunction up to x = 20, using the step size
x = 0
i = 1
while x <= 20:
   #add each point the y array
   wf_points.append(((-wf_points[i-1]+wf_points[i]+wf_points[i+1])-(2*(d**2)*z(x_points[i])*wf_points[i])))
   x_points.append((x0+((i+2)*d)))
   #add each point to the x array
   x = x_points[i]
   i = i+1

print(x_points)
print(wf_points)

#plot the wavefunction 
plot1 = plt.figure(1)
plt.plot(x_points,wf_points,'r-')
plt.ylabel("ψ(x)")
plt.xlabel("x")


#square the wavefunction to get the probability amplitude
k = 0
wf_points_squared = [0]*len(wf_points)
while k < len(wf_points): 
    wf_points_squared[k] = (wf_points[k])**2
    k = k +1

#print the results
plot2 = plt.figure(2)
plt.plot(x_points,wf_points_squared,'r-')
plt.ylabel("$|ψ(x)|^2$")
plt.xlabel("x")

plt.show()



