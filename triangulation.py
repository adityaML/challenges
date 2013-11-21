import numpy as np
import sys,os
import scipy.optimize


def get_angle(v1,v2):
	angle = np.arccos(np.dot(v1, v2))
	if np.isnan(angle):
		if (v1 == v2).all():
			return 0.0
		else:
			return np.pi
	return angle

if __name__=='__main__':
	l2norm= lambda p,x: np.linalg.norm(p-x)
	# three landmark points
	p=np.array([[18.2153969,-210.61306,-157.08696],[35.1232319,-203.58668,-156.28716],[23.93357,-208.93555,-154.09246]])
	# distances to those landmarks from TCD measuring device
	r=np.array([45,66,50])
	f=lambda x: sum([(l2norm(p[i,:],x)-r[i])**2 for i in range(3)])
	xopt=scipy.optimize.fmin(func=f,x0=np.array([0,0,0]))
	print xopt
	x1=np.array([24.38606,-208.122063,-154.290117])
	print 'Dist 1 from x1 and device : ' + str(l2norm(xopt,x1)) # which is around 52.130268 mm
	x2=np.array([28.69695,-204.3147,-153.483399])
	print 'Dist 2 from x2 and device : ' + str(l2norm(xopt,x2)) # which is around 57.6163 mm 
	x3=np.array([33.1367,-203.1093,-153.727])
	print 'Dist 3 from x3 and device : ' + str(l2norm(xopt,x3)) # which is around 62.1453 mm
	x4=np.array([21.7625,-209.567,-155.588])
	print 'Dist 4 from x4 and device : ' + str(l2norm(xopt,x4)) # which is around 49.2357 mm
	x5=np.array([25.609,-206.9585,-154.018])
	print 'Dist 5 from x5 and device : ' + str(l2norm(xopt,x5)) # which is around 53.7129 mm
	# Inlet coordinates from profile [31.6551,-203.41296,-153.58512]
	# normal at the Inlet  : [-0.937234,-0.27345,0.21636]
	In=np.array([31.6551,-203.41296,-153.58512])
	In_normal=np.array([-0.937234,-0.27345,0.21636])
	vector1=xopt-In
	unitvector1= vector1 / np.linalg.norm(vector1)
	angle_at_Inlet=get_angle(unitvector1,In_normal)
	print angle_at_Inlet , unitvector1
	Out=np.array([20.9665,-209.584,-155.942])
	Out_normal=np.array([-0.813885,-0.136188,-0.564839])
	vector2=xopt-Out
	unitvector2 = vector2/ np.linalg.norm(vector2)
	angle_at_Outlet=get_angle(unitvector2,Out_normal)
	print angle_at_Outlet , unitvector2
	###########
	x6=np.array([20.9665,-209.584,-155.942])
	print "Distance from Inlet: "+str(l2norm(xopt,x6))+" mm"
	# Doubt in time of measurement  
	# plane.xtr measurements, it is at a distance of 53.7129mm
	center = np.array([25.609,-206.9585,-154.018])
	normal = np.array([0.7239,0.6756,0.1392])
	
	
	
	