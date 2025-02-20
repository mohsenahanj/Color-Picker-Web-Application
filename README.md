### Color Picker Web Application
![Screenshot 2025-02-21 021357](https://github.com/user-attachments/assets/ef161ff6-7f85-492f-ae0f-f78c139e3231)
## Description

**Color Picker** is a web application built using Flask that allows you to upload images and identify the dominant colors present in them. The application uses the K-Means algorithm to detect up to 9 dominant colors and displays them in HEX, RGB, and CMYK formats. Additionally, it adjusts the text color based on the brightness of each color and provides a "Copy HEX" button for easy copying of color codes.

---

## Features

- **Image Upload:** Users can upload their images.
- **Dominant Color Detection:** Uses K-Means clustering to identify 9 dominant colors in the image.
- **Color Filtering:** Filters out similar colors to ensure only distinct colors are displayed.
- **Color Display:** Displays dominant colors with their HEX, RGB, and CMYK values.
- **Copy HEX Code:** Allows users to easily copy the HEX code of each color.
- **User-Friendly UI:** A clean and responsive design using CSS.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/color-picker.git
   cd color-picker

Create a virtual environment (optional but recommended):
  ```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
  ```bash
pip install -r requirements.txt
```
Run the application:
  ```bash
python app.py
```

Open the application in your browser:
  ```bash
[python app.py](http://127.0.0.1:5000)
```

**Usage**
After running the application, go to http://127.0.0.1:5000 in your browser.
Select and upload an image.
The dominant colors in the image will be displayed along with their HEX, RGB, and CMYK codes.
You can copy the HEX code of any color by clicking the "Copy HEX" button.
Requirements
To run this project, you need the following dependencies:

-Python 3.6+
-Flask
-Pillow
-NumPy
-scikit-learn

These dependencies are listed in the requirements.txt file. You can install them using:
  ```bash
pip install -r requirements.txt
```

**Folder Structure**
  ```bash
/color-picker
    app.py
    /static
        /uploads
        screenshot.png
        example_output.png
    /templates
        index.html
    requirements.txt
```
app.py: The main application code.
/static/uploads: Directory for storing uploaded images.
/templates/index.html: HTML template for the web page.
requirements.txt: List of required Python packages.
README.md: This file!


**Contributing**
If you'd like to contribute to this project, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes and commit them (git commit -m 'Add some feature').
Push your changes to your branch (git push origin feature/YourFeature).
Submit a pull request.


**License**
This project is licensed under the MIT License .


**Acknowledgments**
-[Flask]([https://choosealicense.com/](https://flask.palletsprojects.com/en/stable/?spm=5aebb161.71ee6924.0.0.43c7c921BxLDxj))
-Pillow
-NumPy
-scikit-learn

**Contact**
If you have any questions or feedback, feel free to reach out:

     ```markdown
     - Email: ahanjm@gmail.com
     - GitHub: [@mohsenahanj](https://github.com/mohsenahanj)
     ```
