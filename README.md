# Depthscanner
Imports 3D points from an Intel Realsense Depth Camera into Rhino Grasshopper.

## Dependencies
- compas
- pyrealsense2 (python version 2.7)
- numpy
- scipy

## Author

Ilmar Hurkxkens <<hurkxkens@arch.ethz.ch>> [@ilmihur](https://github.com/ilmihur/)

## Getting Started

To be able to connect to the Depth Camera, you have to install the *Intel Realsense SDK* and also the package management system *Anaconda* to install the dependencies of the `depthscanner` library: 

- [Intel® RealSense™ SDK 2.0](https://www.intelrealsense.com/developers/)
- [Anaconda](https://www.anaconda.com/distribution/)

Once you have Anaconda installed, open `Anaconda Prompt` as administrator. First, create a new conda environment using python 3.7 and make it active: 

    $ conda create -n my_env python=3.7
    $ conda activate my_env
    
Now install `COMPAS` and the `pyrealsense2` libraries to interface with the Intel Realsense Depth Camera (note: numpy and scipy will be automatically installed as well): 

    $ conda config --add channels conda-forge
    $ conda install COMPAS
    $ pyhton -m compas_rhino.install -v 6.0
    $ pip install pyrealsense2
    
Clone the depthscanner repository from github to your local drive, and install the package in your active conda environment:
    
    $ git clone https://github.com/ilmihur/depthscanner.git  
    $ local_folder\ pip install -e depthscanner
    
To verify your setup, start Python from the command line and run the following (when nothing happens the installation is successful):

    $ python
    
    >>> import compas
    >>> import pyrealsense2
    >>> import depthscanner

Now fetch the grasshopper file and scan away :)
