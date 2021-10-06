'''
This file contains combined code for bearing test 1 and needs to be modified incase other outputs are desired.
'''
import numpy as np 	# linear algebra
import pandas as pd	 # data processing, CSV file I/O (e.g. pd.read_csv)
import os

# Incase Data is from external source: This function can be used.
def formulate_dataset(in_dir):
    final_data = pd.DataFrame()
    for filename in os.listdir(in_dir):
        print(filename)
        df=pd.read_csv(os.path.join(in_dir, filename), sep='\t', header=None)
        df['filename'] = os.path.basename(filename)
        df1= pd.DataFrame(df)
        df1.columns = ['x1','y1','x2','y2', 'x3','y3','x4','y4','Class']
        dfs=[final_data, df1]
        final_data = final_data.append(df1) 
        print(final_data)
    return final_data
data_test1_dir = '../input/bearing-dataset/1st_test/1st_test'
df1 = formulate_dataset(data_test1_dir) 
# df1.to_csv('test1.csv',index=False)


# Incase Data is already present
start_time = time.time()
df=pd.read_csv(r'../input/imstest1/test1.csv', delimiter=',')
print("--- Executed in %s seconds ---" % (time.time() - start_time))

#Sort the data based on time / here class==timestamp
import time
start_time = time.time()
df1 = df.sort_values('Class', ignore_index=True)
print("--- Executed in %s seconds ---" % (time.time() - start_time))

#Working on x1 column
my_data=df
my_data=my_data['x1']
print("Data: ",my_data," Size: ",my_data.size)

#Variables and initial Datastructures
from numpy import genfromtxt                #CSV TO NUMPY
from scipy.fftpack import fft			  #FREQ FEATURES	
import matplotlib.pyplot as plt             #PLOT 
import copy                                 #DATA PROCESSING


start=0
slide=8192       			#(FOR WINDOWING)WITHIN TIME SAMPLE FRAMING
window=20480     	#(FOR SAMPLING)SIZE OF TIME SAMPLE STUDIED AT 1 PT. OF TIME
sample=np.empty((0,window))                		#TIME SAMPLE
time_features=np.empty((0,5))   			#TIME DOMAIN statistical FEATURES
repeat=int(window/slide)                      	 #TO SEE HOW MANYWINDOWS IN 1 TIME SAMPLE
hamming=np.hamming(slide)                   				#HAMMING WINDOW 
fft_fea=np.empty((0))                    			 #FREQ DOMAIN  STATISTICAL FEATURES
combined_val=np.empty((0,6))             			 #FEATURE VECTOR AND LABEL FILE
freq_features=np.empty((0,int(window/slide),int(slide/2)-1)) #time_Sample,no. of sliding windows in time sample, no.of fft

#For making Time Samples
import time
start_time = time.time()
count=0
while((start+window) <= (my_data.size)):
    print("Size: (",start,",",start+window,")",count)
    slice1=copy.copy(my_data[start:start+window])
    sample = np.append(sample, [slice1],0 )
    start=start+slide
    count=count+1   
print(sample)
print("--- %s seconds ---" % (time.time() - start_time))


# Getting the Time Domain Features
import time
start_time = time.time()
i=0
while(i<count):
    #print(i)
    min_val=np.min(sample[i])
    max_val=np.max(sample[i])
    std_val=np.std(sample[i])
    rms_val= np.sqrt(np.mean(sample[i]**2))
    grad=np.mean(np.gradient(sample[i]))
    temp_array=[min_val,max_val,std_val,rms_val,grad]
    time_features=np.append(time_features, [temp_array],0)
    i=i+1
print(time_features)    
print("--- Executed in %s seconds ---" % (time.time() - start_time))
print(len(time_features)) #Total Features


#FREQUENCY-DOMAIN FEATURES FOR x1
start_time = time.time()
i=0
fea_counter=0
slide=8192
while(i<count):
    print(i)
    start=0
    freq_sample=np.empty((0,int(slide/2)-1))
    while (start+slide<=window):
        fft_value=fft(sample[i][start:start+slide]*hamming)
        fft_val = 2.0/slide * np.abs(fft_value[1:int(slide/2)]) 
        freq_sample = np.append(freq_sample, [fft_val],0)
        psd=np.mean(fft_val[i]**2)
        fft_fea=np.append(fft_fea, [psd],0)
        start=start+slide
    freq_features=np.append(freq_features,[freq_sample],0)
    i=i+1
print(fft_fea.shape)
print(freq_features.shape)
print("--- Executed in %s seconds ---" % (time.time() - start_time))


