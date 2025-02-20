# Color Picker Web Application
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
  ```
  ```
Create a virtual environment (optional but recommended):
  ```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
  ```bash
pip install -r requirements.txt
```
