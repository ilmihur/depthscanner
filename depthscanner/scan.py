# First import the libraries
import pyrealsense2 as pyrs
import numpy as np
from scipy.interpolate import griddata

def scangrid(): 

    # Declare pointcloud object, for calculating pointclouds and texture mappings
    pc = pyrs.pointcloud()
    # We want the points object to be persistent so we can display the last cloud when a frame drops
    points = pyrs.points()
    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = pyrs.pipeline()
    #Start streaming with default recommended configuration
    profile = pipe.start()
    # to figgure out the depth scale, normally 0.001
    #depth_sensor = profile.get_device().first_depth_sensor()
    #print depth_sensor.get_depth_scale()

    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()
        # Fetch depth frames
        depth = frames.get_depth_frame()
        
        points = pc.calculate(depth)

        pts = np.asanyarray(points.get_vertices())
        
        # use: from scipy.interpolate import griddata
        # https://earthscience.stackexchage.com/questions/12057/how-to-interpolate-scattered-data-to-a-regular-grid-in-python/
        # use a mask to mask-out the outline..
        
        # values to return to rhino
        return pts
          
        # convert to numpy array	
        #npy_vtx = np.zeros((len(vtx), 3), float)
        #for i in range(len(vtx)):
        #    npy_vtx[i][0] = np.float(vtx[i][0])
        #    npy_vtx[i][1] = np.float(vtx[i][1])
        #    npy_vtx[i][2] = np.float(vtx[i][2])

    finally:
        pipe.stop()


def scan(): 

    # Declare pointcloud object, for calculating pointclouds and texture mappings
    pc = pyrs.pointcloud()
    # We want the points object to be persistent so we can display the last cloud when a frame drops
    points = pyrs.points()
    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = pyrs.pipeline()
    #Start streaming with default recommended configuration
    profile = pipe.start()
    # to figgure out the depth scale, normally 0.001
    #depth_sensor = profile.get_device().first_depth_sensor()
    #print depth_sensor.get_depth_scale()

    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()
        # Fetch depth frames
        depth = frames.get_depth_frame()
        # calculate point cloud
        points = pc.calculate(depth)
        # get vertices
        pts = np.asanyarray(points.get_vertices())
        #return the list of vertices to rhino
        return pts

    finally:
        pipe.stop()
