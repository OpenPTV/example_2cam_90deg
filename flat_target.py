import numpy as np

flat_target = np.zeros((66,4))
# id 
flat_target[:,0] = range(1,67)

# column by column fill x
flat_target[:11,1] = 0.0
flat_target[11:22,1] = 10.0
flat_target[22:33,1] = 20.0
flat_target[33:44,1] = 30.0
flat_target[44:55,1] = 40.0
flat_target[55:,1] = 50.0

# column by column fill y
flat_target[:11,2] = np.arange(0,11*10,10.)
flat_target[11:22,2] = np.arange(0,11*10,10.)
flat_target[22:33,2] = np.arange(0,11*10,10.)
flat_target[33:44,2] = np.arange(0,11*10,10.)
flat_target[44:55,2] = np.arange(0,11*10,10.)
flat_target[55:,2] =   np.arange(0,11*10,10.)


#shift the 0,0 to the center of the plate
flat_target[:,1] -= 25.0
flat_target[:,2] -= 50.0

np.savetxt('flat_target.txt',flat_target, fmt = '%d \t %6.4f \t %6.4f \t %6.4f')