import numpy as np
import pyfftw
from scipy.signal import hilbert
from psutil import cpu_count
from scipy.signal import detrend as scipy_detrend
pyfftw.interfaces.cache.enable()

class FreqFeatures:
    def __init__(self, df):
        self.x = df    
    '''
    Frequency Domain Features
    y = signal of FFT 
    f = Frequency of FFT
    Y = Amplitude of FFT / Spectrum Values
    df = Frequency spacing in Hz
    X = Shaft speed in Hz
    D = Pitch diameter
    d = roller diameter
    n = Number of rollers
    theta = Contact angle in degrees
    bearing = 1D array of Bearing characteristic frequencies in orders (i.e. per revolution)
        bearing[0] - Inner race
        bearing[1] - 2x roller spin frequency
        bearing[2] - Cage frequency
        bearing[3] - Outer race frequency
    sf = Sampling frequency
    Detrend = optional string that detrends the signal using scipy.signal.detrend
         'constant' to remove mean value
         'linear' to remove least squares fit
         'none' to do nothing
    hann =  optional for adding a hanning window if true.
    cons = optional parameter to check whether conservative part of the spectrum should be returned:
         True returns sf/2.56 
         False returns sf/2.0 
    '''

    def analytic_signal(self):
        '''This function returns the original signal'''
        return hilbert(self.x)

    def fft(self, y, sf, detrend='constant', hann=True, cons=True):  
        y = np.array(y)
        n = y.size
        T = n/sf
        # Check if conservative output is desired
        if cons:
            Fmax = sf/2.56
        else:
            Fmax = sf/2.0
        # number of lines
        numL = int(T*Fmax)
        # mean is removed if desired
        if detrend != 'none':
            y = scipy_detrend(y, type=detrend)
        # for hanning window
        if hann is True:
            y = np.hanning(y.size)*y
        # Discrete Fourier Transform
        Y = self.rawfft(y)
        df = 1.0/T
        return np.abs(Y[0:numL])*2.0/n, np.fft.fftfreq(numL,df), df

    def rawfft(self, y):    
        y = np.array(y, copy=True)
        Yobject = pyfftw.builders.fft(y, 
                                    auto_align_input=True, 
                                    auto_contiguous=True, 
                                    planner_effort='FFTW_ESTIMATE', 
                                    overwrite_input=True
                                )
        return Yobject()   

    def maxPowerSpectrum(self, y):
        fourier= self.rawfft(y)
        abs_ft = np.abs(fourier[0])
        ps= np.square(abs_ft)
        return np.max(ps)    

    def maxEnvelope(self,y):
        y = np.abs(y)
        return np.max(y)
            
    def frequencyCenter(self, Y, f):
        return np.sum(f*Y)/np.sum(Y)

    def rootMeanSquareFrequency(self, Y,f):
        return (np.sum(f**2*Y)/np.sum(Y))**0.5

    def VarianceFrequency(self, Y, f):
        fi=np.mean(f)
        return np.sum(((f-fi)**2)*Y)/np.sum(Y)

    def rootVarianceFrequency(self, f, Y):
        fi=np.mean(f)
        return (np.sum(((f-fi)**2)*Y)/np.sum(Y))**0.5

    def medianFrequency(self, Y, df):
        cumsum = np.cumsum(Y)
        return np.argmin(np.abs(cumsum - 0.5*cumsum[-1]))*df
    
    def bearingcharfrequencies(D, d, n, theta=0.0):
        theta = theta*np.pi/180.0
        FTF = 1.0/2.0 * (1.0 - d/D*np.cos(theta))
        BPFO = n*FTF
        BPFI = n/2.0 * (1.0 + d/D*np.cos(theta))
        BSF = D/(2.0*d) * (1.0 - (d/D * np.cos(theta))**2.0)
        #gives bearing = Bearing fault orders (inner, roller, cage, outer)
        return np.array([BPFI, 2*BSF, FTF, BPFO])

    def bearingEnergy(Y, df, X, bearing):
        lowerFrequency = np.min([bearing[0], bearing[1], bearing[3]])*X*0.95
        upperFrequency = np.max([bearing[0], bearing[1], bearing[3]])*X*1.05
        i1 = int(np.floor(lowerFrequency/df))
        i2 = int(np.ceil(upperFrequency/df))
        return np.sum(Y[i1:i2+1])