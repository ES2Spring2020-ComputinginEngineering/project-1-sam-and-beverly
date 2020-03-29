# Some Code To Help with Data Logging Processing and Graphing
# Jenn Cross
# ******************************************************

import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.constants as cons

data34cm = np.genfromtxt('dataset1_34cm.csv', delimiter=',')
data43cm = np.genfromtxt('dataset2_43cm.csv', delimiter=',')
data53cm = np.genfromtxt('dataset3_53cm.csv', delimiter=',')
data62cm = np.genfromtxt('dataset4_62cm.csv', delimiter=',')
data72cm = np.genfromtxt('dataset5_72cm.csv', delimiter=',')

#Crop arrays to clean data rows
data34cm =  data34cm[500:1300,:]
data43cm =  data43cm[500:1300,:]
data53cm =  data53cm[500:1300,:]
data62cm =  data62cm[500:1300,:]
data72cm =  data72cm[500:1300,:]

#Calculate accelerations in G units from milliG (and time from milliseconds to seconds)
data34cm =  data34cm/1000
data43cm =  data43cm/1000
data53cm =  data53cm/1000
data62cm =  data62cm/1000
data72cm =  data72cm/1000

#Calculate Theta and Apply Median Filter (Window size =3)
theta34 = sig.medfilt(np.arctan2(data34cm[:,1], np.sqrt(data34cm[:,2] ** 2) + (data34cm[:,3] ** 2)), 3)
theta34 = scipy.signal.medfilt(theta34)
theta43 = sig.medfilt(np.arctan2(data43cm[:,1], np.sqrt(data43cm[:,2] ** 2) + (data43cm[:,3] ** 2)), 3)
theta43 = scipy.signal.medfilt(theta43)
theta53 = sig.medfilt(np.arctan2(data53cm[:,1], np.sqrt(data53cm[:,2] ** 2) + (data53cm[:,3] ** 2)), 3)
theta53 = scipy.signal.medfilt(theta53)
theta62 = sig.medfilt(np.arctan2(data62cm[:,1], np.sqrt(data62cm[:,2] ** 2) + (data62cm[:,3] ** 2)), 3)
theta62 = scipy.signal.medfilt(theta62)
theta72 = sig.medfilt(np.arctan2(data72cm[:,1], np.sqrt(data72cm[:,2] ** 2) + (data72cm[:,3] ** 2)), 3)
theta72 = scipy.signal.medfilt(theta72)

#Calculate Average Period
def get_period(dataset, timeset):
    time_index=timeset[:,0]
    peak, _ =scipy.signal.find_peaks(dataset)
    plt.plot(time_index[peak], theta34[peak], 'r-')
    plt.title('Peaks')
    plt.tight_layout()
    plt.show()
    period=np.diff(time_index[peak])
    period=np.mean(period)
    return period
period_34=get_period(theta34, data34cm)
period_43=get_period(theta43, data43cm)
period_53=get_period(theta53, data53cm)
period_62=get_period(theta62, data62cm)
period_72=get_period(theta72, data72cm)
#Calculate accelerations in m/s^2 units (cons.g is 9.80665 m/s^2)
data34cm[:, 1:3] =  data34cm[:, 1:3]*cons.g
data43cm[:, 1:3] =  data43cm[:, 1:3]*cons.g
data53cm[:, 1:3] =  data53cm[:, 1:3]*cons.g
data62cm[:, 1:3] =  data62cm[:, 1:3]*cons.g
data72cm[:, 1:3] =  data72cm[:, 1:3]*cons.g

#Graphs of Accelerations and Theta
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8], sharex=True)
ax1.plot(data34cm[:,0], data34cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 34cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data34cm[:,0], data34cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data34cm[:,0], data34cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data34cm[:,0], theta34[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data43cm[:,0], data43cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 43cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data43cm[:,0], data43cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data43cm[:,0], data43cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data43cm[:,0], theta43[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data53cm[:,0], data53cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 53cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data53cm[:,0], data53cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data53cm[:,0], data53cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data53cm[:,0], theta53[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data62cm[:,0], data62cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 62cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data62cm[:,0], data62cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data62cm[:,0], data62cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data62cm[:,0], theta62[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=[10,8],sharex=True)
ax1.plot(data72cm[:,0], data72cm[:,1], "#9467bd")
ax1.set_title('X Accel vs Time, Length 72cm')
ax1.set_ylabel ('Acceleration (m/s^2)')    
ax2.plot(data72cm[:,0], data72cm[:,2], "#17becf")
ax2.set_title('Y Accel vs Time')
ax2.set_ylabel ('Acceleration (m/s^2)')
ax3.plot(data72cm[:,0], data72cm[:,3], "#2ca02c")
ax3.set_title('Z Accel vs Time')
ax3.set_ylabel ('Acceleration (m/s^2)')
ax4.plot(data72cm[:,0], theta72[:], "#ff7f0e")
ax4.set_title('Theta vs Time')
ax4.set_ylabel ('Theta (rad)')
plt.xlabel('Time (s)')
plt.tight_layout()
plt.show()

print(period_34)
print(period_43)
print(period_53)
print(period_62)
print(period_72)