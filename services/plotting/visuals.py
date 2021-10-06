import matplotlib.pyplot as plt

'''
For plotting actual Signals
'''
import matplotlib.pyplot as plt  
f = plt.figure(figsize=(10,10))
plt.subplot(2, 2, 1)
plt.plot(df['bx1'])
plt.title('bx1')
plt.subplot(2, 2, 2)
plt.plot(df['by1'])
plt.title('by1')
plt.subplot(2, 2, 3)
plt.plot(df['bx2'])
plt.title('bx2')
plt.subplot(2, 2, 4)
plt.plot(df['by2'])
plt.title('by2')
plt.show()


'''
For Frequency vs Amplitude Graphs after results are obtained
'''
f = plt.figure(figsize=(12,12))
plt.subplot(2, 2, 1)
plt.plot(fd['fft'][1],fd['fft'][0])
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('bx1')
plt.subplot(2, 2, 2)
plt.plot(fd1['fft'][1],fd1['fft'][0])
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('by1')
plt.subplot(2, 2, 3)
plt.plot(fd2['fft'][1],fd2['fft'][0])
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('bx2')
plt.subplot(2, 2, 4)
plt.plot(fd3['fft'][1],fd3['fft'][0])
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('by2')
plt.show()