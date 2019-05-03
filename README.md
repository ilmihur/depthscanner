# Depthscanner
Collects a PointCloud from a 3D scanner

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

## Installation:
- open Anaconda Prompt as administrator
- create a conda environment with python 2.7 `conda create -n scanner python=2.7`
- change to the newly created environment `conda activate scanner`
- install compas `conda install COMPAS`
- install pyrealsense2 `pip install pyrealsense2`

- clone the depthscanner repository from github `git clone https://github.com/ilmihur/depthscanner.git`
- install the package you just downloaded on your computer: `pip install %UserProfile%/depthscanner`
