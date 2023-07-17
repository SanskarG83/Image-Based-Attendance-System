# Image-Based-Attendance-System

- This image Based attendance System automated the traditional way of Attendance systems. 
- This system uses LBPH algorithm to detect images and Student's faces.


# Getting started
1. Clone the repository:
https://github.com/SanskarG83/Image-Based-Attendance-System.git

2. Install the required dependencies:

3. Download the LBPH model weights and place them in the models directory.


# NOTE

Preferred python version : 3.8.5


# Algorithm

-- Linear Binary Pattern Histogram --
1. Dividing the face image into small regions and computing the Local Binary Pattern (LBP) for each region.
2. Constructing a histogram of the local binary patterns for the entire face.
3. Comparing the computed histograms with the stored histograms of known faces to determine the identity.

#DEMO:

https://github.com/SanskarG83/Image-Based-Attendance-System/assets/100311018/a01fee4b-241b-4843-a092-d68105578840
