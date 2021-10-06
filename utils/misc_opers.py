import pandas as pd
import json
from services.features.freq_domain import FreqFeatures
from services.features.time_domain import TimeFeatures
from numpyencoder import NumpyEncoder
from utils.complex import ComplexEncoder
class Misc:
   def __init__(self, df, feature, testset):
       self.df =df
       self.feature=feature
       self.testset = testset
    
   def fetch_df(self):
       if self.testset == 1:
           df = pd.read_csv(r'datasets\\IMScsv\\test1.csv', delimiter=',')
       elif self.testset == 2:
           df = pd.read_csv(r'datasets\\IMScsv\\test2.csv', delimiter=',')
       elif self.testset == 3:
           df = pd.read_csv(r'datasets\\IMScsv\\test3.csv', delimiter=',')
       else:
           return
       return df
    
   def sort_df(self):
       return self.df.sort_values(self.feature, ignore_index=True)

   def features(self, attr):
       reqd =[]
       result = {}
       result['Test Set'] = self.testset
       if attr == 'x1' or attr == 'bx1':
           result['Bearing'] = 1
           result['Channel'] = 1
       elif attr == 'y1' or attr == 'by1':
           result['Bearing'] = 1
           result['Channel'] = 2
       if attr == 'x2' or attr == 'bx2':
           result['Bearing'] = 2
           result['Channel'] = 1
       elif attr == 'y2' or attr == 'by2':
           result['Bearing'] = 2
           result['Channel'] = 2
       if attr == 'x3' or attr == 'bx3':
           result['Bearing'] = 3
           result['Channel'] = 1
       elif attr == 'y3' or attr == 'by3':
           result['Bearing'] = 3
           result['Channel'] = 2       
       if attr == 'x4' or attr == 'bx4':
           result['Bearing'] = 4
           result['Channel'] = 1
       elif attr == 'y4' or attr == 'by4':
           result['Bearing'] = 4
           result['Channel'] = 2  
       
       x1=TimeFeatures(self.df[attr])             
       td = {}
       td['mean'] = x1.mean()
       td['absoluteMean'] = x1.absoluteMean()
       td['std'] = x1.standardDeviation()
       td['var'] = x1.variance()
       td['maxA'] = x1.maxAmplitude()
       td['minA'] = x1.minAmplitude()
       td['rms'] = x1.rms()
       td['p2p'] = x1.peakToPeak()
       td['skewness'] = x1.skewness()
       td['skewnessFactor'] = x1.skewnessFactor()
       td['kurtosis'] = x1.kurtosis()
       td['kurtosisFactor'] = x1.kurtosisFactor()
       td['clearanceFactor'] = x1.clearanceFactor()
       td['shapeFactor'] = x1.shapeFactor()
       td['crestFactor'] = x1.crestFactor()
       td['impulsiveFactor'] = x1.impulseFactor()
       td['sum'] = x1.sum()
       td['log'] = x1.LOG()
       td['entropyF'] = x1.entropyFactor(0.2)
       result['Time Domain Features'] = td
       
       fd = {}
       x2 = FreqFeatures(self.df[attr])  
       fd['signal'] = x2.analytic_signal()
       fd['fft'] = x2.fft(fd['signal'], 1024)
       fd['maxpowerspectrum'] = x2.maxPowerSpectrum(fd['signal'])
       fd['maxEnvelope']=x2.maxEnvelope(fd['signal'])
       fd['frequencyCenter']=x2.frequencyCenter(fd['fft'][0],fd['fft'][1])
       fd['rootMeanSquareFrequency']=x2.rootMeanSquareFrequency(fd['fft'][0],fd['fft'][1])
       fd['varianceFrequency']=x2.VarianceFrequency(fd['fft'][0],fd['fft'][1])
       fd['rootVarianceFrequency']=x2.rootVarianceFrequency(fd['fft'][0],fd['fft'][1])
       fd['medianFrequency']=x2.medianFrequency(fd['fft'][0],fd['fft'][2])
       
       result['Frequency Domain Features'] = fd
       reqd.append(result)

       name = 'results\\'+'testset'+str(result['Test Set'])+'-'+'bearing'+str(result['Bearing'])+'-'+'Channel'+str(result['Channel'])+'.json'
       # Writing to sample.json
       with open(name, 'w+') as fp:
           try:
               json.dump(reqd, fp)
           except:
               json.dump(reqd, fp, cls = ComplexEncoder)
       return reqd


