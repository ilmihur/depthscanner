# First import the libraries
import compas
import pyrealsense2 as pyrs
import numpy as np
from scipy.interpolate import griddata

def dfScan():
 
    # set the resolution
    xres = 1280
    yres = 720

    # Declare pointcloud object, for calculating pointclouds and texture mappings
    pc = pyrs.pointcloud()
    # We want the points object to be persistent so we can display the last cloud when a frame drops
    points = pyrs.points()
    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = pyrs.pipeline()
    # Create a config and configure the pipeline to stream
    config = pyrs.config()
    #set resolution
    config.enable_stream(pyrs.stream.depth,  xres, yres, pyrs.format.z16, 30)
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

        ## take only values that are not zero
        ptss = []
        for i in pts:
            if i[0] != 0:
                ptss.append(i)
     
        ## make x,y,z lists
        x = []
        y = []
        z = []
        for i in ptss:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        
        #bounding box of scan
        x_min = -0.64 #min(x)
        x_max = 0.64 #max(x)
        y_min = -0.36 #min(y)
        y_max = 0.36 #max(y)

        #target grid to interpolate to
        xi = np.arange(x_min,x_max,0.001)
        yi = np.arange(y_min,y_max,0.001)
        xi,yi = np.meshgrid(xi,yi)

        # interpolate
        zi = griddata((x,y),z,(xi,yi),method='linear',fill_value=0)
    	#zi = np.nan_to_num(zi,copy=False)

        ## set mask
        #mask = (xi > 0.5) & (xi < 0.6) & (yi > 0.5) & (yi < 0.6)

        ## mask out the field
        #zi[mask] = np.nan

        ## reformat z data to docofossor (single list of z values)
        np.flipud(zi)
        zi *= -1
        zi = [j for i in zi for j in i]
        zi = [i * 1000 for i in zi]

        # construct docofossor dimension list
        nc = xres #len(zi[0]) >>> see target grid in scangrid
        nr = yres #len(zi) >>> see target grid in scangrid
        ox = 0
        oy = 0
        cx = 1 #1*n
        cy = 1 #1*n
        gx = ox
        gy = oy
        dim = [nc,nr,ox,oy,cx,cy,0,0,gx,gy]
        
        # construct df list
        df = dim + zi

        #trying to send a string to grasshopper instead of a list
        #df = ' '.join("%.2f" % i for i in df)
        
        # values to return to rhino
        return df

    finally:
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
