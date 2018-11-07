# Mea-Kanu

Mea Kanu is a mobile application that uses Plant Identification through leading edge machine learning and artificial intelligence techniques known as fine grain categorization. The major technologies involved are python, javascript, HTTP,back end as a service (BaaS), artificial intellgence, neural networks, machine learning. 

1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [App Information](#App-Information)

## Introduction

The application is trained to accurately identify 100 different plant species found around the island.
In order to train the neural network, 4500 images were collected from various sources and compiled into a file system. The 
folders were then analyzed over the course of a week using segmentation. The resulting product is a highly accurate, fast, and responsive application.

The plant identification script is currently loaded onto a local HTTP python server. The app was originally planned to be hosted on a cloud based server, but the neural network is a large file (~130 Mb), and we did not want to incur hosting costs. Future plans include moving the entire Mea Kanu architecture into the cloud, specifically Amazon Web Services.

On the front end the Application uses Nativescript with Vue. This allows our application to be transpiled into working Android and iOS applications.



Mea Kanu translates from Hawaiian as Plant 

## Installation

### Running the server locally:

  In order to run the server several python libraries must be installed. 
  
  Start by first installing python 3 on your corresponding operating system as follows:
  
  ##### Note: If at any point a permission error appears, prepend the installation command with sudo or open the terminal in
  #####       administrator mode on Windows
  
  ####  Windows:
  
  1.  Open a browser window and navigate to the Download page for Windows at python.org.
  
  2.  Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3    
      Release - Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
  
  3.  Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable  
      installer for 32-bit. (See below.)
      
  4.  Important: You want to be sure to check the box that says Add Python 3.x to PATH as shown to ensure that the   
      interpreter will be placed in your execution path.
      
  5.  Run the installer. 
      
      
   #### Mac:
    
    brew install python3
    
   #### Linux (Ubuntu):
   
   Install python3 by opening the terminal and enter the follwoing commands:
   
   ```
   $ sudo apt-get update
   $ sudo apt-get install python3.6
   ```
   
   Verify a successful install by entering the following command and verifying version number:
   
   ```
   $ python --version
     python 3.6.5
   ```

Once python is installed, pip3 should be installed with it. Use this to install the rest of the dependencies.
The server and machine learning program use several libraries as listed below:

#### Machine Learning Libraries
* tensorflow
* keras
* cv2

#### Encoding Libraries
* base64

To install the machine learning libraries start with tensorflow:

```pip3 install tensorflow```

Once the tensorflow package is installed the Keras package can be installed:

```pip3 install keras```

Finally the cv2 library can be added

#### Windows

Follow the steps found on the CV2 website found [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html)

#### Mac

#### Linux

Enter the following command:

```
$ sudo apt-get install python-opencv
```

Verify the installation with:

```
$ python
>>>import cv2 as cv
>>>print(cv2.__version__)
3.4.3
>>>
```
If no errors appear the library has successfully been installed.

The encoding libary base 64 is the only installation remaining and can be done with the following command:

```
pip install pybase64
```
Once all the dependencies have been installed the server can be succesfully hosted on a local machine. Get the public IP address of your machine [here](www.whatsmyip.com) assign the IP address and desired port in the final two lines of the server code and run the server using:

```
python3 server.py
```

Connect to the host from any front end service and send a HTTP POST request with any image file to classify the image.

The application can take any image and classify what type of plant it is.

## App Information

This mobile phone application takes pictures from your phones camera or gallery then 
Privacy Policy. Our App asks for permission to use your device's camera and its file system so that you can take/upload pictures of plants.
