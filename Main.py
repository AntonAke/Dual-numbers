from Dual import *
import time
import numpy as np
import matplotlib.pyplot as plt

"""Calculates the error for numerical differentiation
of a function for different x:es when h varies"""
def error(minh, maxh, dualFunc, realFunc, stepnum, xlist):
    for x in xlist:
        steps = stepnum/x
        value = dualFunc(Dual(x,1)).getDual()
        deviation = [abs((realFunc(x+h)-realFunc(x-h))/(2*h)-value)
                     for h in np.linspace(minh, maxh, steps)]
        plt.plot(np.linspace(minh, maxh, steps), deviation,
                 label = "x = " + str(x))
    plt.ylim(10**(-16), 10**(4))
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('h')
    plt.ylabel('Avvikelse')
    plt.legend()
    plt.show()

#Compares runtime for automatic and numerical differentiation        
def times(min, max, dualFunc, realFunc, steps): 
    inp = [Dual(val, 1) for val in np.linspace(min, max, num=steps)]
    start = time.time()
    derivatives = [dualFunc(x) for x in inp]
    end = time.time()
    print("Automatisk: " + str(end-start) + "s")
       
    inp =  [x.getReal() for x in inp]
    def numerical(x):
        eps = (2.2*10**(-16))**0.5
        h = (eps*x if x!= 0 else eps)
        return (realFunc(x+h)-realFunc(x-h))/(2*h)
    start = time.time()
    derivatives2 = [numerical(x) for x in inp]
    end = time.time()
    print("Numerisk: " + str(end-start) + "s")

"""Plots a function and its derivative between min and max,
using automatic differentiation"""
def plot(min, max, dualFunc):
    inp = [Dual(val, 1) for val in np.linspace(min, max, 10000)]
    ans = [dualFunc(x) for x in inp]

    values = [d.getReal() for d in ans]
    derivatives = [d.getDual() for d in ans]
    inp =  [d.getReal() for d in inp]

    plt.plot(inp, values, "b")
    plt.plot(inp, derivatives, "r")
    plt.show()

#Dual and regular example functions
def exDualFunc1(x):
    return Dual.log(Dual.pow(Dual.cos(x),2)*Dual.cosh(x)
          +Dual.atan(Dual.pow(x,2)))/Dual.exp(Dual.cosh(Dual.atan(x)))

def exRealFunc1(x):
    return math.log(math.pow(math.cos(x),2)*math.cosh(x)
          +math.atan(math.pow(x,2)))/math.exp(math.cosh(math.atan(x)))
    
def exDualFunc2(x):
    return Dual.pow(x,3)

def exRealFunc2(x):
    return math.pow(x,3)


#Runtime, plot and error for example functions
def timeExample():
    times(0, 10, exDualFunc1, exRealFunc1, 100000)
    
def plotExample():
    plot(0, 10, exDualFunc1)
    
def errorExample():
    error(10**(-16),10**(-6), exDualFunc2, exRealFunc2,
             5000, [0.001, 0.1, 10])




