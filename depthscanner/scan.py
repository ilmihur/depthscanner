# First import the libraries
import compas
import pyrealsense2 as pyrs
import numpy as np
from scipy.interpolate import griddata
from timeit import default_timer as timer

#here start the scanner
# Declare RealSense pipeline, encapsulating the actual device and sensors

_pipe = None
_pipe = pyrs.pipeline()

def get_pipe():
    global _pipe
    return _pipe

def dfScan():

    ### send param
    #def dfScan(some_param):
    #print(some_param)

    start = timer()

    # set the resolution
    xres = 640
    yres = 360
    
    # Declare pointcloud object, for calculating pointclouds and texture mappings
    pc = pyrs.pointcloud()
    # We want the points object to be persistent so we can display the last cloud when a frame drops
    points = pyrs.points()
    pipe = get_pipe()
    # Create a config and configure the pipeline to stream
    config = pyrs.config()
    #set resolution
    config.enable_stream(pyrs.stream.depth, xres, yres, pyrs.format.z16, 30)
    #Start streaming 
    profile = pipe.start(config)

    ## to figgure out the depth scale, normally 0.001
    #depth_sensor = profile.get_device().first_depth_sensor()
    #print depth_sensor.get_depth_scale()

    
    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()
        # Fetch depth frames
        depth = frames.get_depth_frame()
        # calc pointcloud
        points = pc.calculate(depth)
        #w = depth.get_width()
        #h = depth.get_height()
        
        # get point coordinates
        pts = np.asanyarray(points.get_vertices())
        print('1',timer()-start)
        ## take only values that are not zero
        
        ## numpy nonzero 
        ptss = []
        for i in pts:
            if i[0] != 0:
                ptss.append(i)

        print('2',timer()-start)
     
        ## make x,y,z lists
        x = []
        y = []
        z = []
        for i in ptss:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        print('3', timer()-start)
        
        #bounding box of scan
        x_min = -0.6 #min(x)
        x_max = 0.6 #max(x)
        y_min = -0.4 #min(y)
        y_max = 0.4 #max(y)

        #target grid to interpolate to
        xi = np.arange(x_min,x_max,0.002)
        yi = np.arange(y_min,y_max,0.002)
        xi,yi = np.meshgrid(xi,yi)
             
        print('4', timer()-start)

        # interpolate
        zi = griddata((x,y),z,(xi,yi),method='cubic',fill_value=0.6)
    	#zi = np.nan_to_num(zi,copy=False)
        print('5', timer()-start)
        ## set mask
        #mask = (xi > 0.5) & (xi < 0.6) & (yi > 0.5) & (yi < 0.6)

        ## mask out the field
        #zi[mask] = np.nan

        ## reformat z data to docofossor (single list of z values)
        zi = [j for i in zi for j in i]
        zi = [i * 1000 for i in zi]

        ## flip etc..
        ## zi = zi[::-1]
        ## zi *= -1
        
        # construct docofossor dimension list
        nc = 600 #len(zi[0]) >>> see target grid in scangrid
        nr = 400 #len(zi) >>> see target grid in scangrid
        ox = -585
        oy = 390
        cx = 2 #1*n
        cy = 2 #1*n
        gx = ox
        gy = oy
        dim = [nc,nr,ox,oy,cx,cy,0,0,gx,gy]
        
        # construct df list
        df = dim + zi

        #trying to send a string to grasshopper instead of a list
        #df = ' '.join("%.2f" % i for i in df)

        # CONVERT TO base64
        #import base64 >>
        # otherwise png
        
        
        print('6', timer()-start)
        # values to return to rhino
        return df

    finally:  ### dont stop it
        pipe.stop()

def pcScan(): 

    # Declare pointcloud object, for calculating pointclouds and texture mappings
    pc = pyrs.pointcloud()
    # We want the points object to be persistent so we can display the last cloud when a frame drops
    points = pyrs.points()
    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = pyrs.pipeline()
    #Start streaming 
    profile = pipe.start()

    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()
        # Fetch depth frames
        depth = frames.get_depth_frame()
        # calculate point cloud
        points = pc.calculate(depth)
        # get vertices
        pts = np.asanyarray(points.get_vertices())
        ## take only values that are not zero (removes about 2/3 of the points)
        ptss = []
        for pt in pts:
            if pt[0] != 0:
                r = [i * 1000 for i in pt] #scale by 1000
                ptss.append(r)
        #return the list of vertices to rhino
        print(pts[0])
        print(ptss[0])
        return ptss
       
    finally:
        pipe.stop()

if __name__ == "__main__":
    s = dfScan()
