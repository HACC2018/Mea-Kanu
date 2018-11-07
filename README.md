# Mea-Kanu

Mea Kanu is a mobile application taht uses Plant Identification through leading edge machine learning and artificial intelligence techniques known as fine grain categorization. The major technologies involved are python, javascript, HTTP,back end as a service (BaaS), artificial intellgence, neural networks, machine learning. 

The application is trained to accurately identify 100 different plant species found around the island.
In order to train the neural network, 4500 images were collected from various sources and compiled into a file system. The 
folders were then analyzed over the course of a week using segmentation. The resulting product is a highly accurate, fast, and responsive application.

The plant identification script is currently loaded onto a local HTTP python server. The app was originally planned to be hosted on a cloud based server, but the neural network is a large file (~130 Mb), and we did not want to incur hosting costs. Future plans include moving the entire Mea Kanu architecture into the cloud, specifically Amazon Web Services.

On the front end the Application uses Nativescript with Vue. This allows our application to be transpiled into working Android and iOS applications.



Mea Kanu translates from Hawaiian as Plant 

Running the server locally:
  In order to run this program several python libraries must be installed. 
  
  Start by first installing python 3 on your corresponding operating system as follows:
    Windows:
      Open a browser window and navigate to the Download page for Windows at python.org.
      Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3       Release - Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
      Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit. (See below.)
      Important: You want to be sure to check the box that says Add Python 3.x to PATH as shown to ensure that the interpreter will be placed in your execution path.
      
      Run the installer. 
      
      
    Mac:
    
    
    Linux (Ubuntu):
    
    $ sudo apt-get update
    $ sudo apt-get install python3.6
    
    verify installation by opening the terminal and typing the following command:
    python3 --version
    
    your output should be similar to the following:
    python 3.6.5
  

This mobile phone application takes pictures from your phones camera or gallery then 
Privacy Policy. Our App asks for permission to use your device's camera and its file system so that you can take/upload pictures of plants.
