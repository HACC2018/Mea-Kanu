# Mea-Kanu

Mea Kanu is a mobile application that uses Plant Identification through leading edge machine learning and artificial intelligence techniques known as fine grain categorization. The major technologies involved are python, javascript, HTTP,back end as a service (BaaS), artificial intellgence, neural networks, machine learning. 

1. [Introduction](#Introduction)
2. [Installation](#Installation)

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
  #####           administrator mode on Windows
  
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

#### Server Libraries
* base64
* json

To install the machine learning libraries start with tensorflow:

```pip install tensorflow```

Once the tensorflow package is installed the Keras package can be installed:

```pip install keras```

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

```
This mobile phone application takes pictures from your phones camera or gallery then 
Privacy Policy. Our App asks for permission to use your device's camera and its file system so that you can take/upload pictures of plants.
