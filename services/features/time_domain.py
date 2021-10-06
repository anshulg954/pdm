from math import log
import numpy as np
from scipy.stats import entropy

class TimeFeatures:
    '''
    Class: Time Domain Features
    x = input vib
    p= a sequence of the (discrete) distribution 
       where p[i] is the (possibly unnormalized) probability of event i.
    '''

    def __init__(self, df):
        self.x = df

    def mean(self):
        return np.mean(self.x)
 
    def absoluteMean(self):
        return np.mean(np.abs(self.x))
 
    def standardDeviation(self):
        return np.std(self.x)
 
    def variance(self):
        return np.var(self.x)
 
    def maxAmplitude(self):
        return np.max(self.x)
 
    def minAmplitude(self):
        return np.min(self.x)   
 
    def rms(self):    
        rms = np.sqrt(np.sum(self.x**2)/self.x.size)
        return rms
 
    def peakToPeak(self):
        return np.max(self.x) + np.min(self.x)
 
    def squareMeanRoot(self):
        return np.sum(np.sqrt(np.abs(self.x)))**2

    def standardMoment(self, k):
        xk = (self.x - np.mean(self.x))**k
        x2 = (self.x - np.mean(self.x))**2
        SM = np.mean(xk)/np.mean(x2)**(float(k)/2.0)
        return SM,xk

    def skewness(self):
        return self.x.skew()
 
    def skewnessFactor(self):
        return self.standardMoment(3)[0]/self.rms()**3
 
    def kurtosis(self):
        x2 = np.abs(self.x - np.mean(self.x))**2.0
        K = np.mean(x2**2.0)/self.standardDeviation()**4
        return K
 
    def kurtosisFactor(self):
        return self.standardMoment(4)[0]/self.rms()**4
 
    def clearanceFactor(self):
        return np.max(self.x)/self.squareMeanRoot()
 
    def shapeFactor(self):
        return self.rms()/self.absoluteMean()
 
    def impulseFactor(self):
        return np.max(self.x)/self.absoluteMean()
 
    def crestFactor(self):
        return np.max(self.x)/self.rms()
 
    def sum(self):
        return np.sum(self.x)
 
    def LOG(self):
        return np.exp(np.mean(np.log(np.abs(self.x))))  

    def entropyFactor(self,p):
        return entropy(p, base=2)

    
    