# Depthscanner
Imports 3D points from an Intel Realsense Depth Camera into Rhino Grasshopper.

## Dependencies
- compas
- pyrealsense (python version 2.7)
- numpy
- scipy

## Author

Ilmar Hurkxkens <<hurkxkens@arch.ethz.ch>> [@ilmihur](https://github.com/ilmihur/)

## Getting Started

The recommended way to install **depthscanner** is to use [Anaconda/conda](https://conda.io/docs/). Once you have Anaconda installed, open `Anaconda Prompt` as administrator and follow the steps below.

Create a new conda environment using python 2.7 and make it active: 

    $ conda create -n scanner python=2.7
    $ conda activate scanner
    
Now install `COMPAS` and the `pyrealsense2` libraries to interface with the Intel Realsense Depth Camera (note: numpy and scipy will be automatically installed as well): 

    $ conda install COMPAS
    $ pip install pyrealsense2
    
Clone the depthscanner repository from github to your local drive, and install the package in your active conda environment:
    
    $ git clone https://github.com/ilmihur/depthscanner.git  
    $ pip install %UserProfile%/depthscanner
    
Now fetch the grasshopper file and scan away :)


## Notes to self:
For more info on package creation and metadata see:
https://python-packaging.readthedocs.io/en/latest/minimal.html
