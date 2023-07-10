Image Processing Application

This is an image processing application built using Python and the PySide6 library. It allows users to select an image folder, view and select images from the folder, and apply image processing operations on the selected image.
Libraries Used

    Python - The programming language used to develop the application.
    PySide6 - The cross-platform GUI toolkit for Python used to create the application's graphical interface.
    OpenCV - The computer vision library used for image processing and contour detection.

Features

    Browse and select an image folder.
    Display a list of valid image files in the selected folder.
    View and select an image from the list.
    Process the selected image by applying image contour detection and saving the processed image.
    Display the coordinates of the detected contours.
    Save the coordinates to a text file.
    Show a success message upon image processing completion.
    
## Installation

1. Clone the repository:

   
   git clone https://github.com/your-username/image-processing-app.git
   

2. Change to the project directory:

   
   cd image-processing-app
  

3. Install the required dependencies using pip:

   
   pip install -r requirements.txt
  

## Usage

1. Run the application:

   python main.py
   

2. The application window will open.
3. Click the "Browse" button to select an image folder.
4. The list of valid image files in the selected folder will be displayed.
5. Select an image from the list to view it in the image viewer.
6. Click the "Proceed" button to process the selected image.
7. The processed image will be saved as "processedimage.png" in the current directory.
8. The coordinates of the detected contours will be saved in a text file named "coordinates.txt" in the current directory.
9. A success message will be displayed upon image processing completion.
