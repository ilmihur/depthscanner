# Depthscanner
Collects a PointCloud from the Intel Realsense 3D scanner in Rhino Grasshopper.

## Dependencies
- compas
- pyrealsense (python version 2.7)
- numpy
- scipy

## Notes to self:
for more info on package information and metadata see:
https://python-packaging.readthedocs.io/en/latest/minimal.html

## Author

Ilmar Hurkxkens <<hurkxkens@arch.ethz.ch>> [@ilmihur](https://github.com/ilmihur/)

## Getting Started

The recommended way to install **depthscanner** is to use [Anaconda/conda](https://conda.io/docs/). Once you have Anaconda installed, open `Anaconda Prompt` as administrator and follow the steps below.

Create a new conda environment using python 2.7: 

    $ conda create -n scanner python=2.7
    
Change to the newly created environment: 

    $ conda activate scanner
    
Install COMPAS (note: numpy and scipy will be automatically installed as well): 

    $ conda install COMPAS
    
Install `pyrealsense2` to interface with the Intel Realsense Depth Camera: 
    
    $ pip install pyrealsense2
    
Clone the depthscanner repository from github to your local drive: 
    
    $ git clone https://github.com/ilmihur/depthscanner.git
    
Install the package you just downloaded in your conda environment: 
    
    $ pip install %UserProfile%/depthscanner
    
Now fetch the grasshopper file and scan away :)
