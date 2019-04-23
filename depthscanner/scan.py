def test():
    x = 5
    return x

def scan(): #### and set all one tab forward

    ## License: Apache 2.0. See LICENSE file in root directory.
    ## Copyright(c) 2017 Intel Corporation. All Rights Reserved.

    #####################################################
    ##                  Export to PLY                  ##
    #####################################################

    # First import the library

    import pyrealsense2 as rs

    # Declare RealSense pipeline, encapsulating the actual device and sensors
    pipe = rs.pipeline()
    #Start streaming with default recommended configuration
    pipe.start()

    try:
        # Wait for the next set of frames from the camera
        frames = pipe.wait_for_frames()

        # Fetch color and depth frames
        depth = frames.get_depth_frame()
        color = frames.get_color_frame()

        ldist = []
        for y in range(480):
            for x in range(640):
                dist = depth.get_distance(x, y)
                ldist.append(dist)

        #print(len(ldist))

        return ldist
        
    finally:
        pipe.stop()
